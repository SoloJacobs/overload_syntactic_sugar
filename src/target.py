from sol import GetItem

# reveal_type(GetItem())

_: GetItem

def f(_: GetItem) -> None:
    ...

class Test(GetItem):
    a: int
