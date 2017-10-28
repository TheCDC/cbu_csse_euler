#!/usr/bin/env python3
from itertools import permutations
import multiprocessing as mp


def generate_pandigitals(start=1, stop=None):
    if stop is None:
        stop = 10
    for i in range(start, stop):
        yield from permutations(set(range(1, i + 1)))


def list_to_num(l, b=10):
    n = 0
    for i in l:
        n = n * b + i
    return n


def isPrime(n):
    """Return whether a number is prime."""
    # handle base cases
    if n <= 0 or n % 2 == 0:
        return False
    elif n == 2:
        return True
    elif n == 1:
        return False
    for i in range(3, int(n**(1 / 2)) + 1, 2):
        if n % i == 0:
            return False
    return True


def process_num(digits):
    n = list_to_num(digits)
    if isPrime(n):
        return n
    else:
        return 0


def main():
    pool = mp.Pool()
    results = pool.map(process_num, generate_pandigitals())
    print(max(results))
    # print(max(map(process_num, generate_pandigitals())))


if __name__ == '__main__':
    main()
