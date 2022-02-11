from __future__ import annotations

from typing import Callable, TypeVar, Generic, Iterable

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)
S = TypeVar('S')
U = TypeVar('U')

__all__ = [
    "Undefined",
    "BaseFunctor",
    "IterableFunctor",
    "BoolPredicate",
]


class Undefined:
    pass


class BaseFunctor(Generic[T, S]):

    def __init__(self, functor: Callable[[T], S]):
        self.functor = functor

    def __ror__(self, other: T) -> S:
        return self.functor(other)


class IterableFunctor(BaseFunctor[Iterable[T_co], Iterable[S]]):

    def __init__(self, functor: Callable[[Iterable[T_co]], Iterable[S]]):
        super().__init__(functor)

    def __ror__(self, other: Iterable[T_co]) -> Iterable[S]:
        return self.functor(other)


class BoolPredicate(Generic[T_co]):

    def __init__(self, function: Callable[[T_co], bool]):
        self.function = function

    def __and__(self, other: BoolPredicate[T_co]) -> BoolPredicate[T_co]:
        return BoolPredicate[T](lambda arg: self(arg) and other(arg))

    def __or__(self, other: BoolPredicate[T_co]):
        return BoolPredicate[T](lambda arg: self(arg) or other(arg))

    def __call__(self, arg: T_co) -> bool:
        return self.function(arg)
