import random


__all__ = [
    "gen_rand",
]


def gen_rand(start: int, end: int):
    while True:
        yield random.randint(start, end)
