from mypy.plugin import Plugin


class CustomPlugin(Plugin):
    def get_type_analyze_hook(self, fullname: str) -> None:
        # see explanation below
        if fullname.startswith("sol.GetItem"):
            print(fullname)


def plugin(version: str) -> type[CustomPlugin]:
    # ignore version argument if the plugin works with all mypy versions.
    return CustomPlugin
