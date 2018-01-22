import functools


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


@functools.lru_cache(maxsize=None)
def primes_up_to(pmax):
    primes = [2] + [n for n in range(3, pmax, 2) if is_prime(n)]
    return primes


def main():
    max_val = 10**6
    print('Generating primes up to {}...'.format(max_val))
    primes = primes_up_to(max_val)
    pset = set(primes)
    print('Found {} primes.'.format(len(primes)))
    longest = -1
    longest_prime = -1
    for i in range(len(primes)):
        chain = 0
        total = 0
        for j in range(i, len(primes)):
            total += primes[j]
            chain += 1
            if total > max_val:
                break
            if total in pset and chain > longest:
                longest = chain
                longest_prime = total
    return longest_prime 


if __name__ == '__main__':
    print(main())
