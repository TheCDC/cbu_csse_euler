#!/usr/bin/env python3
import multiprocessing as mp
from itertools import permutations
digits = set(range(10))


def generate_pandigitals():
    yield from permutations(set(range(10)))


def list_to_num(l, b=10):
    n = 0
    for i in l:
        n = n * b + i
    return n


DIVISORS = [1, 2, 3, 5, 7, 11, 13, 17]


def check_substr_divibility(l):
    for idx, p in reversed(list(enumerate(DIVISORS))):
        n = list_to_num(l[idx:idx + 3], 10)
        if n % p != 0:
            return False
    return True


def check_num(digit_list):
    if check_substr_divibility(digit_list):
        return list_to_num(digit_list)
    else:
        return 0


def main():
    pool = mp.Pool()
    results = pool.map(check_num, generate_pandigitals())
    # results = map(check_num, permutations(set(range(10))))
    print(sum(results))


if __name__ == '__main__':
    main()
