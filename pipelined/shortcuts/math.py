from pipelined.utils import predicate


@predicate
def is_prime(x: int) -> bool:
    k = 2
    while k * k <= x:
        if x % k == 0:
            return False

        k += 1
    else:
        return True


def squared(x: int) -> int:
    return x ** 2


@predicate
def is_even(x: int) -> bool:
    return x % 2 == 0


@predicate
def is_odd(x: int) -> bool:
    return x % 2 != 0


@predicate
def is_positive(x: int) -> bool:
    return x > 0


@predicate
def is_negative(x: int) -> bool:
    return x < 0
