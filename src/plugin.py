from typing import Callable

from mypy.nodes import TypeInfo
from mypy.plugin import FunctionContext, MethodContext, Plugin
from mypy.typeops import make_simplified_union, try_getting_str_literals
from mypy.types import NoneType, Type


class CustomPlugin(Plugin):
    def get_method_hook(
        self, fullname: str
    ) -> None | Callable[[MethodContext], Type]:
        if fullname.endswith("get"):
            return getitem_get_callback
        return None

    def get_function_hook(
        self, fullname: str
    ) -> None | Callable[[FunctionContext], Type]:
        if fullname == "sol.field":
            return field_callback
        return None


def match_single_arg_literals(
    ctx: FunctionContext | MethodContext,
) -> None | list[str]:
    match ctx.arg_types:
        case [[key_type]]:
            return try_getting_str_literals(ctx.args[0][0], key_type)
    return None


def field_callback(ctx: FunctionContext) -> Type:
    keys = match_single_arg_literals(ctx)
    if keys is None:
        return ctx.default_return_type
    return NoneType()


def getitem_get_callback(ctx: MethodContext) -> Type:
    default_return_type = ctx.default_return_type

    type_info = getattr(ctx.type, "type", None)
    if not isinstance(type_info, TypeInfo) or not any(
        base.serialize() == "sol.Get" for base in type_info.bases
    ):
        return default_return_type

    keys = match_single_arg_literals(ctx)
    if keys is None:
        return default_return_type

    types = []
    for key in keys:
        if key not in type_info.names:
            return default_return_type
        type_ = type_info.names[key].type
        if type_ is None:
            return default_return_type
        types.append(type_)
    return make_simplified_union(types)


def plugin(version: str) -> type[CustomPlugin]:
    # TODO: check what version this plug-in is compatible with.
    # ignore version argument if the plugin works with all mypy versions.
    return CustomPlugin
