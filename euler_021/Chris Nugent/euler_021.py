from functools import lru_cache
from math import ceil


def divisors(n):
    divs = {1}
    for i in range(2, ceil(n**(1 / 2))):
        if n % i == 0:
            divs.update([i, n // i])
    return divs


@lru_cache(maxsize=None)
def d(n):
    return sum(divisors(n))


def main(n):
    known = set()
    for a in range(1, n):
        b = d(a)
        db = d(b)
        if db == a and a != b:
            known.update([a, b])
    return sum(known)


if __name__ == "__main__":
    print(main(10000))
