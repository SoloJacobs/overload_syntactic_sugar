from typing import Callable

from mypy.plugin import FunctionContext, MethodContext, Plugin
from mypy.typeops import try_getting_str_literals
from mypy.types import NoneType, Type


class CustomPlugin(Plugin):
    def get_type_analyze_hook(self, fullname: str) -> None:
        if fullname.startswith("sol.GetItem"):
            print(f"get_type_analyze_hook({fullname})")

    def get_base_class_hook(self, fullname: str) -> None:
        if fullname.startswith("sol.GetItem"):
            print(f"get_base_class_hook({fullname})")

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


def plugin(version: str) -> type[CustomPlugin]:
    # ignore version argument if the plugin works with all mypy versions.
    return CustomPlugin
