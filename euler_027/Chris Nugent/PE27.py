import functools
import multiprocessing


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


def f(a):
    # print('Checking for a = {}'.format(a))
    best_a, best_b = None, None
    best = -1
    for b in range(-999, 999, 2):
        n = 0
        test = b
        while is_prime(test):
            n += 1
            test = (n * n) + (a * n) + b
        if n > best:
            best = n
            best_b = b
    return a, best_b, best


main():
    threads = 4
    amax = 1000
    pool = multiprocessing.Pool(threads)

    print('Running with {} threads...'.format(threads))
    m = pool.map(f, range(-amax, amax))
    vals = max(m, key=lambda x: x[2])
    print('n^2 + {}n + {} produced {} consecutive primes.'.format(*vals))

if __name__ == '__main__':
    main()
