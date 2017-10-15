from utils import divisors
from functools import lru_cache


@lru_cache(maxsize=1000)
def d(n):
    return sum(divisors(n))


def main():
    known = set()
    for a in range(10000):
        b = d(a)
        db = d(b)
        if db == a and b != a and not set((a, b)) & known:
            # print(a, b)
            known.add(a)
            known.add(b)

    # print(d.cache_info())
    print(sum(known))


if __name__ == '__main__':
    main()
