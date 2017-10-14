from euler_043 import *


def factorial(n):
    c = 1
    while n > 1:
        c *= n
        n -= 1
    return c


def test_generate_pandigitals():
    """Check that exactly `10!` pandigitals are generated."""
    cases = [
        (0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (1, [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]),
        (2, [0, 1, 2, 3, 4, 5, 6, 8, 7, 9]),
        (3, [0, 1, 2, 3, 4, 5, 6, 8, 9, 7]),
        (4, [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]),
        (5, [0, 1, 2, 3, 4, 5, 6, 9, 8, 7]),
        (6, [0, 1, 2, 3, 4, 5, 7, 6, 8, 9]),
        (7, [0, 1, 2, 3, 4, 5, 7, 6, 9, 8]),
        (8, [0, 1, 2, 3, 4, 5, 7, 8, 6, 9]),
        (9, [0, 1, 2, 3, 4, 5, 7, 8, 9, 6]),

    ]
    g = generate_pandigitals()
    for c in cases:
        index = c[0]
        val = c[1]
        d = next(g)
        assert d == val
    count = 0
    for _ in generate_pandigitals():
        count += 1
    assert count == factorial(10)


def test_check_substr_divibility():
    assert check_substr_divibility(list(map(int, "1406357289")))


def test_list_to_num():
    cases = [
        (([1, 2, 3], 10), 123),
        (([1, 0, 0], 10), 100),
        (([1], 10), 1),
        (([2], 10), 2),
        (([9, 9, 9, 9], 10), 9999),
        (([5, 4, 3, 2, 1, 0], 10), 543210),
    ]
    for c in cases:
        args = c[0]
        val = c[1]
        assert list_to_num(*args) == val
