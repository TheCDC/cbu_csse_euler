import itertools
import logging


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


def tuple_to_int(tup):
    n = 0
    for i in tup:
        n *= 10
        n += i
    return n


def main():
    largest = 0
    for n in range(9, 0, -1):
        logging.info('Checking {}-digit pandigitals...'.format(n))
        numbers = range(1, n + 1)
        for p in itertools.permutations(numbers):
            pandigital = tuple_to_int(p)
            if pandigital > largest and is_prime(pandigital):
                largest = pandigital
        if largest != 0:
            return largest
        logging.info('No {}-digit pandigital primes.'.format(n))
    return -1


if __name__ == '__main__':
    n = str(main())
    print('{} is the largest pandigital prime, with {} digits.'
          .format(n, len(n)))
