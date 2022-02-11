import functools
from typing import Callable, Iterable, TypeVar

from .core import (
    BoolPredicate, IterableFunctor,
)

T_co = TypeVar('T_co', covariant=True)
S = TypeVar('S')


def predicate(function):
    return BoolPredicate(function)


def enable_pipe(
    function: Callable[[Iterable[T_co]], Iterable[S]]
) -> IterableFunctor[T_co, S]:
    return IterableFunctor(function)


def enable_pipe_factory(function):
    @functools.wraps(function)
    def decorator(*args, **kwargs):
        @enable_pipe
        def wrapper(data: Iterable[T_co]) -> Iterable[S]:
            return function(data, *args, **kwargs)

        return wrapper

    return decorator
