Sometimes I write code like this:

```
import typing


class A(typing.Protocol):
    @typing.overload
    def get(self, key: typing.Literal["a"]) -> int:
        ...

    @typing.overload
    def get(self, key: typing.Literal["b"]) -> str:
        ...

    @typing.overload
    def get(self, key: typing.Literal["a", "b"]) -> int | str:
        ...
```

However, I would much rather implement a special `Get` class, which allows me use syntax very similiar to `TypedDict`:

```
class A(Get):  # Should do the same as the definition above.
    a: int
    b: str
```
