from euler_055 import *


def test_is_lychrel():
    s = """196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986, 1495, 1497, 1585, 1587, 1675, 1677"""
    cases = map(lambda x: int(x.strip()), s.strip().split(','))
    for c in cases:
        assert is_lychrel(c)
    assert is_lychrel(10677)
    assert is_lychrel(196)
    assert is_lychrel(691)
    assert is_lychrel(4994)
    assert not is_lychrel(47)
    assert not is_lychrel(197)
    assert not is_lychrel(349)
    assert not is_lychrel(4997)
    assert not is_lychrel(89)


def test_next_number():
    cases = [
        (47, 121),
        (349, 1292),
        (1292, 4213),
        (4213, 7337),
    ]
    for c in cases:
        assert next_number(c[0]) == c[1]


def test_is_palindrome():
    cases = [
        121,
        7337,
        99999,
        999,
        12344321,
        55555555,
    ]
    for c in cases:
        assert is_palindrome(c)
