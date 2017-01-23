#!/usr/bin/env python3
"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import utils
import itertools
import pdb


def only_prime_rotations(n):
    ds = utils.digits(n, 10)[::-1]
    for _ in range(len(ds)):
        ds.append(ds.pop(0))
        i = int(''.join(map(str, ds)))
        if not utils.isPrime(i):
            # print(i,"not prime",ds)
            return False
        # print(ds)
    return True


def only_odds(n):
    for d in utils.digits(n, 10):
        if d > 0 and d % 2 == 0:
            return False
    return True


def test(n):
    if n == 2:
        return True
    if only_odds(n):
        if only_prime_rotations(n):
            return True
    return False


def sanity():
    # pdb.set_trace()
    for i in "197, 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 197".split(","):
        n = int(i.strip())
        assert test(n), "{} should pass".format(i)

sanity()


def main():
    cs = []
    c = 1
    # for p in itertools.product(list([str(i) for i in range(1,10,2)]),repeat=6):
    #     print(p)
    #     i = int(''.join(p))
    for i in range(3, 1000000 + 1, 2):
        if test(i):
            c += 1
            cs.append(i)
    print(c)
    # print(cs)

if __name__ == '__main__':
    main()
