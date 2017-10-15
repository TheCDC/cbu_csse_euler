#!/usr/bin/env python3
from utils import isPrime


def main():
    primes = [2, 3]
    i = primes[-1]
    while primes[-1] < 2000000:
        i += 2
        if isPrime(i):
            # print(i)
            primes.append(i)
    primes.pop()
    print(sum(primes))


if __name__ == '__main__':
    main()
