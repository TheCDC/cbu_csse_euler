from euler_043 import *


def factorial(n):
    c = 1
    while n > 1:
        c *= n
        n -= 1
    return c


def test_check_substr_divibility():
    """Check that exactly `10!` pandigitals are generated."""
    count = 0
    for _ in generate_pandigitals():
        count += 1
    assert count == factorial(10)


def test_list_to_num():
    cases = [
        (([1, 2, 3], 10), 123),
        (([1, 0, 0], 10), 100),
        (([1], 10), 1),
        (([2], 10), 2),
        (([9, 9, 9, 9], 10), 9999),
    ]
    for c in cases:
        args = c[0]
        val = c[1]
        assert list_to_num(*args) == val
