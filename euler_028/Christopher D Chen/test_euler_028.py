from euler_028 import *


def test_corner_sum():
    cases = [
        (0, 1),
        (1, 7 + 9 + 5 + 3),
        (2, 21 + 25 + 13 + 17),
    ]
    for c in cases:
        assert corner_sum(c[0]) == c[1]


def test_super_sum():
    cases = [
        (0, 1),
        (1, 25),
        (2, 101),
    ]
    for c in cases:
        assert super_sum(c[0]) == c[1]
