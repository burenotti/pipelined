from typing import Callable, Iterable, Reversible, TypeVar

from .utils import enable_pipe
from .core import IterableFunctor

T = TypeVar('T')
S = TypeVar('S')

__all__ = [
    "apply",
    "where",
    "order_by",
    "sort",
    "reverse",
    "first_n"
]


def apply(function: Callable[[T], S]) -> IterableFunctor[Iterable[T], Iterable[S]]:
    @enable_pipe
    def wrapper(other: Iterable[T]) -> Iterable[S]:
        return map(function, other)

    return wrapper


@enable_pipe
def reverse(other: Reversible[T]) -> Iterable[T]:
    return reversed(other)


def where(function: Callable[[T], bool]) -> IterableFunctor[Iterable[T], Iterable[T]]:
    @enable_pipe
    def wrapper(other: Iterable[T]) -> Iterable[T]:
        return filter(function, other)

    return wrapper


def order_by(
    key: Callable[[T], S] = None,
    reverse: bool = False
) -> IterableFunctor[Iterable[T], Iterable[T]]:
    @enable_pipe
    def ordering(data: Iterable[T]) -> Iterable[T]:
        return sorted(data, key=key, reverse=reverse)

    return ordering


sort: IterableFunctor[Iterable, Iterable] = order_by(key=None, reverse=False)


def first_n(n: int):
    @enable_pipe
    def wrapper(data: Iterable[T]) -> Iterable[T]:
        return (item for _, item in zip(range(n), data))

    return wrapper
