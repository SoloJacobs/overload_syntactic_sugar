from mypy.plugin import Plugin


class CustomPlugin(Plugin):
    def get_type_analyze_hook(self, fullname: str) -> None:
        if fullname.startswith("sol.GetItem"):
            print(f"get_type_analyze_hook({fullname})")

    def get_base_class_hook(self, fullname: str) -> None:
        if fullname.startswith("sol.GetItem"):
            print(f"get_base_class_hook({fullname})")



def plugin(version: str) -> type[CustomPlugin]:
    # ignore version argument if the plugin works with all mypy versions.
    return CustomPlugin
