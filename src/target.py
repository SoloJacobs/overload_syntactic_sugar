from sol import GetItem

# reveal_type(GetItem())

# Unwanted syntax

_: GetItem

def f(_: GetItem) -> None:
    ...

# Wanted syntax

class Test(GetItem):
    a: int
