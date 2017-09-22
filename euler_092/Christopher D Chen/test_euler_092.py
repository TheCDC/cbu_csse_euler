from euler_092 import *


def test_digits():
    cases = [
        (123, [1, 2, 3]),
        (0, [0]),
        (4321, [4, 3, 2, 1]),
        (99999, [9, 9, 9, 9, 9]),
    ]
    for c in cases:
        assert digits(c[0]) == c[1]


def test_permuted():

    cases = [
        (44, 32),
        (32, 13),
        (13, 10),
        (1, 1),
        (85, 89),
        (89, 145),
        (145, 42),
        (42, 20),
        (20, 4),
    ]
    for c in cases:
        assert permuted(c[0]) == c[1]
