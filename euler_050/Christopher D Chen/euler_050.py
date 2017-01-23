#!/usr/bin/env python3

"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


"""Strategy:
We are looking for a prime equal to the sum of n consecutive primes.
n must be odd because all primes except 2 are odd and odd+odd=even.
"""

from utils import isPrime
from itertools import product


def partials(l):
    return [sum(l[:i]) for i in range(len(l))]

MAX = 1000000
primes = [2]
for i in range(1, MAX, 2):
    if isPrime(i):
        primes.append(i)
        
lsums = partials(primes)
rsums = partials(primes[::-1])[::-1]


def psum(a, b):
    return sum(primes[a: b])


def slice_is_prime(a, b):
    return isPrime(psum(a, b))


def main():
    # cursors
    c1 = 0
    c2 = 0
    sp = psum(c1, c2)
    print("ceiling")
    while sp < MAX:
        c2 += 1
        sp = psum(c1, c2)
    print("reducing ceiling")
    while not isPrime(sp):
        c2 -= 1
        sp = psum(c1, c2)
    print("optimizing")
    go = True
    while go:
        offsets = [-1, 0, 1, -2, 2]
        for p in product(offsets, repeat=2):
            if slice_is_prime(c1 + p[0], c2 + p[1]) and (((c2 + p[1]) - (c1 + p[0])) > (c2 - c1)) and psum(c1 + p[0], c2 + p[0]) < MAX:
                print(c1, c1, p)
                c1 += p[0]
                c2 += p[1]
            else:
                go = False
    sp = sum(primes[c1:c2])
    print(c1, c2, c2, c1, primes[c1], primes[c2], sp)
    print(isPrime(sp))
if __name__ == '__main__':
    main()
