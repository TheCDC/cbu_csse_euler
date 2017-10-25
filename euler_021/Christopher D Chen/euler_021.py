from utils import divisors
from functools import lru_cache


@lru_cache(maxsize=None)
def d(n):
    return sum(divisors(n))


def main():
    known = set()
    for a in range(10000):
        b = d(a)  # by definition
        db = d(b)
        # if a and b are amicable
        if db == a and b != a:
            # remember them
            known.add(a)
            known.add(b)

    print(sum(known))


if __name__ == '__main__':
    main()
