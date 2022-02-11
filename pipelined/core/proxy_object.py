from __future__ import annotations
from .functors import BoolPredicate
from typing import Callable, Optional

__all__ = [
    "ProxyObject"
]


class ProxyObject(BoolPredicate):

    def __init__(self, function: Optional[Callable] = None):
        super().__init__(function)
        if function is None:
            self.__function = lambda x: x
        else:
            self.__function = function

    def __getattr__(self, item: str) -> ProxyObject:
        return ProxyObject(lambda obj: self.__function(getattr(obj, item)))

    def __add__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) + other
        )

    def __radd__(self, other):
        return ProxyObject(
            lambda obj: other + self.__function
        )

    def __sub__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) - other
        )

    def __rsub__(self, other):
        return ProxyObject(
            lambda obj: other - self.__function(obj)
        )

    def __mul__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) * other
        )

    def __rmul__(self, other):
        return ProxyObject(
            lambda obj: other * self.__function(obj)
        )

    def __eq__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) == other
        )

    def __gt__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) > other
        )

    def __ge__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) >= other
        )

    def __lt__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) < other
        )

    def __le__(self, other):
        return ProxyObject(
            lambda obj: self.__function(obj) <= other
        )

    def __call__(self, value):
        return self.__function(value)
