import typing

class GetItem(typing.Protocol):
    def get(self, key: str) -> typing.NoReturn:
        ...

def field(key: object) -> typing.NoReturn:
    ...
