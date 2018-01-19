import functools
import multiprocessing
import os
import time


@functools.lru_cache(maxsize=None)
def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num < 0:
        return False
    check = 3
    while check * check <= num:
        if num % check == 0:
            return False
        check += 2
    return True


def f(targs):
    """Solution is setup in this slightly ugly way since it
    was modified on a whim to support multiprocessing"""
    # Even values for b always produce a score of 0, so
    # we only check odds.
    a, bmax = targs
    best_a, best_b = None, None
    best = -1
    for b in range(1, bmax, 2):
        n = 0
        test = b
        while is_prime(test):
            n += 1
            test = (n * n) + (a * n) + b
        if n > best:
            best = n
            best_b = b
    return a, best_b, best


def g(targs):
    """Faster version of f, which works by only testing primes.
    Since f(0) = b, b must be prime for non-zero chains."""
    a, bmax = targs
    bs = primes_up_to(bmax)
    best_b = None
    best = -1
    for b in bs:
        n = 0
        test = b
        while is_prime(test):
            n += 1
            test = (n * n) + (a * n) + b
        if n > best:
            best = n
            best_b = b
    return a, best_b, best


@functools.lru_cache(maxsize=None)
def primes_up_to(pmax):
    print('Thread generating primes lower than {}...'.format(pmax))
    t = tuple([2] + [n for n in range(1, pmax, 2) if is_prime(n)])
    print('Thread found {} primes.'.format(len(t)))
    return t


def main(xmin, xmax, ymax):
    xs = range(xmin, xmax)
    ymaxes = [ymax] * (xmax - xmin)
    threads = os.cpu_count()
    pool = multiprocessing.Pool(threads)
    print('Running with up to {} threads...'.format(threads))
    m = pool.map(g, zip(xs, ymaxes))
    print('Mapping done! Finding maximum...')
    vals = max(m, key=lambda x: x[2])
    print('n^2 + {}n + {} produced {} consecutive primes.'.format(*vals))


if __name__ == '__main__':
    amin, amax, bmax = -999, 1000, 1001
    main(amin, amax, bmax)
