import functools
from typing import (
    List, Dict, Any, Callable, Iterable, Mapping, TypeVar
)

from .utils import enable_pipe
from .core import Undefined, IterableFunctor

__all__ = [
    "to_list",
    "to_dict",
    "reduce",
    "for_each",
    "to",
    "max_by",
    "min_by"
]

T = TypeVar('T')
S = TypeVar('S')


def to(container: type):
    @enable_pipe
    def wrapper(data: Iterable[T]) -> Any:
        return container(data)

    return wrapper


@enable_pipe
def to_list(data: Iterable[T]) -> List[T]:
    return list(data)


@enable_pipe
def to_dict(data: Mapping[T, S]) -> Dict[T, S]:
    return dict(data)


def reduce(function: Callable[[Iterable[T]], S]):
    @enable_pipe
    def wrapper(other: Iterable[T], initial=Undefined):
        if initial is not Undefined:
            return functools.reduce(function, other, initial)
        else:
            return functools.reduce(function, other)

    return wrapper


def for_each(function: Callable[[T], None]):
    @enable_pipe
    def wrapper(other: T):
        for item in other:
            function(item)

    return wrapper


def max_by(key: Callable) -> IterableFunctor[Iterable[T], T]:
    @enable_pipe
    def wrapper(iterable: Iterable[T]) -> T:
        return max(iterable, key=key)

    return wrapper


def min_by(key: Callable):
    @enable_pipe
    def wrapper(iterable: Iterable[T]) -> IterableFunctor[Iterable[T], T]:
        return min(iterable, key=key)

    return wrapper
