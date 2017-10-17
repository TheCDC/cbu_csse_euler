from euler_031 import *


def test_count_configurations():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    cases = [
        (1, 1),
        (2, 2),
        (3, 2),
        (4, 3),
        (5, 4),

    ]
    for c in cases:
        arg = c[0]
        val = c[1]
        assert count_configurations(coins, arg) == val
