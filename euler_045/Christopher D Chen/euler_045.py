#!/usr/bin/env python3
"""Strategy
We are looking for numbers in the intersection of T, P, and H space.
We a way of testing if a given n is n those spaces.
We do that by inverting the T, P, and H functions
"""


def quadratic(a, b, c) -> float:
    sq = (b**2 - 4 * a * c)**(1 / 2)
    denom = 2 * a
    return max((-b + sq) / denom, (-b - sq) / denom)


def tn(n: float) -> float:
    """nth triangle number"""
    return n * (n + 1) / 2


def pn(n: float) -> float:
    """nth pentagonal number"""
    return n * (3 * n - 1) / 2


def hn(n: float) -> float:
    """nth hexagonal number"""
    return n * (2 * n - 1)


def nt(t: float) -> float:
    """n, given a triangle number"""
    return quadratic(1 / 2, 1 / 2, - t)


def np(p: float) -> float:
    """n, given pentagonal number."""
    return quadratic(3 / 2, -1 / 2, -p)


def nh(h: float) -> float:
    """n, given hexagonal number"""
    return quadratic(2, -1, -h)


def test(n: float) -> bool:
    """Map n to triangle space.
    Check if that number is also found in pentagon, hexagon space."""
    a = tn(n)
    return np(a) % 1 == 0 and nh(a) % 1 == 0

# print([nt(i) for i in [1, 3, 6, 10]])
# print([np(i) for i in [1, 5, 12, 22]])
# print([nh(i) for i in [1, 6, 15, 28]])


def sanity():
    # sanity and correctness check
    for i in range(1, 10000):
        assert (nt(tn(i))) == i
        assert (np(pn(i))) == i
        assert (nh(hn(i))) == i
sanity()


def main():
    start = 40755
    i = start + 1
    while not test(i):
        i += 1
    print(tn(i))

if __name__ == '__main__':
    main()
