#!/usr/bin/env python3
import collections
import pprint
import math
from functools import lru_cache


def numprod(l, default=1):
    try:
        p = l[0]
        for i in l[1:]:
            p *= i
        return p
    except IndexError:
        return default


def isPrime(n):
    """Return whether a number is prime."""
    # handle base cases
    if n <= 0:
        return False
    elif n == 2:
        return True
    elif n == 1:
        return False
    try:
        for i in range(2, int(n**(1 / 2)) + 1):
            if n % i == 0:
                return False
    except Exception as e:
        print(e, n)
        raise e
    return True


def primeFactors(n):
    """Return all prime factors of a number.
    Strategy: loop up to sqrt(n), divide n by any prime factors
    found along the way until n is prime."""

    # a base case
    if n == 1:
        return []
    found_factors = []
    # check if reduction is complete
    while not isPrime(n) and n > 1:
        # locate factors below sqrt(n)
        for i in range(2, int(n**(1 / 2)) + 1):
            if n % i == 0 and isPrime(i):
                found_factors.append(i)
                n = n // i
    # 1 will always divide and isn't prime, discard it.
    if n != 1:
        found_factors.append(n)
    found_factors.sort()
    return found_factors


def numDivisors(n):
    """Get the number of divisors of a number.
    Math: Return the product of the sum the powers of the unique prime factors
    incremented by one."""
    if isPrime(n):
        return 2
    c = collections.Counter(primeFactors(n))
    return numprod([i + 1 for i in c.values()])


def divisors(n):
    """Get all divisors of a number."""
    l = [1]
    # only needs to loop to n/2
    for i in range(2, math.ceil(n**(1 / 2))):
        if (n / i) % 1 == 0:
            l.extend([i, n // i])
    return sorted(l)


def nthDigit(n, d, base=10):
    """Find digit at index n."""
    return (n % (base**(d + 1))) // (base**(d))


def numDigits(n, base=10):
    """Get the number of digits of n in base base."""
    if n == 0:
        return 1
    # if n == 1:
    #   return 1
    if base == 1:
        return n

    return math.floor(math.log(n) / math.log(base))


def digits(n, b):
    return [nthDigit(n, i, b) for i in range(numDigits(n, b))]


def numrepr(n, base):

    if base <= 10:
        d = ''
    else:
        d = ':'
    return d.join([str(nthDigit(n, i, base)) for i in range(numDigits(n, base), -1, -1)])


def fact(n):
    p = n
    while n > 1:
        n -= 1
        p *= n
    return p


def main():
    # print(isPrime(3))
    # print(primeFactors(57771))
    # for n in range(2, 10):
    #     for b in [2, 5, 8, 10]:
    #         print(numrepr(n, b), end=' ')
    #     print()
    # print(fact(10))
    # ns = [1, 3, 6, 10, 15, 21, 28] + list(range(1000, 2000)) + [34283340]
    # pprint.pprint([(i, len(divisors(i)), numDivisors(i), (primeFactors(i)))
    #                for i in ns])
    # pprint.pprint([ for i in ns])
    # pprint.pprint([ for i in ns])
    print(numrepr(13456783, 2))


if __name__ == '__main__':
    main()
