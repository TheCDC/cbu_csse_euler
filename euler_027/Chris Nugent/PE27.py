import functools
import multiprocessing
import os

@functools.lru_cache(maxsize=None)
def is_prime(num):
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
    a, bmin, bmax = targs
    if bmin % 2 == 0:
        bmin += 1
    best_a, best_b = None, None
    best = -1
    for b in range(bmin, bmax, 2):
        n = 0
        test = b
        while is_prime(test):
            n += 1
            test = (n * n) + (a * n) + b
        if n > best:
            best = n
            best_b = b
    return a, best_b, best


def main(xmin, xmax, ymin, ymax):
    threads = os.cpu_count()
    print('Detected {} virtual CPUs, running with {} threads...\n'.format(threads, threads))
    pool = multiprocessing.Pool(threads)
    xs = range(xmin, xmax)
    ymins = [ymin] * (xmax - xmin)
    ymaxes = [ymax] * (xmax - xmin)
    m = pool.map(f, zip(xs, ymins, ymaxes))
    vals = max(m, key=lambda x: x[2])
    print('n^2 + {}n + {} produced {} consecutive primes.'.format(*vals))

if __name__ == '__main__':
    main(-999, 1000, -1000, 1001)
