import typing

from sol import GetItem, field

# reveal_type(GetItem())

# Test cases for field


def a_field(x: str) -> None:
    reveal_type(field(x))


def b_field(x: typing.Literal["a", "b"]) -> None:
    reveal_type(field(x))


def c_field(x: str | typing.Literal["a", "b"]) -> None:
    reveal_type(field(x))


reveal_type(field("a", "b"))

# Unwanted syntax

_: GetItem


def f(_: GetItem) -> None:
    ...


# Wanted syntax


class Test(GetItem):
    a: int
    b: str


# Test cases for wanted syntax

t = Test()

reveal_type(t.get("a"))


def a(x: str) -> None:
    reveal_type(t.get(x))


def b(x: typing.Literal["a", "b"]) -> None:
    reveal_type(t.get(x))


def c(x: str | typing.Literal["a", "b"]) -> None:
    reveal_type(t.get(x))


reveal_type(t.get("a", "b"))
