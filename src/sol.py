import typing

class Get(typing.Protocol):
    def get(self, key: str) -> typing.NoReturn:
        ...

def field(key: object) -> typing.NoReturn:
    ...
