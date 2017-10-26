#!/usr/bin/env python3
"""

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either
(i) become a palindrome in less than fifty iterations, or,
(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.

In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
"""

import multiprocessing as mp
from pprint import pprint


def reverse_int(n):
    return int(str(n)[::-1])


def is_palindrome(n):
    return n == reverse_int(n)


def next_number(n):
    return n + reverse_int(n)


class Cache():

    def __init__(self):
        self.memory = dict()
        self.hits = 0
        self.misses = 0

    def get(self, k):
        try:
            self.hits += 1
            return self.memory[k]
        except KeyError as e:
            self.hits -= 1
            self.misses += 1
            raise e

    def set(self, k, v):
        self.memory[k] = v

    def set_and_return(self, k, v):
        self.set(k, v)
        return v

    def __str__(self):
        return 'Cache(hits={}, misses{})'.format(self.hits, self.misses)


lychrel_memory = Cache()


def is_lychrel(n, depth=0):
    # first things first, check the cache
    try:
        return lychrel_memory.get(n)
    except KeyError:
        pass
    # check if we're out of our league
    nn = next_number(n)
    if depth == 50:
        return lychrel_memory.set_and_return(n, True)

    elif is_palindrome(nn):
        return lychrel_memory.set_and_return(n, False)
    else:
        return lychrel_memory.set_and_return(n, is_lychrel(nn, depth + 1))


def main():
    pool = mp.Pool()
    results = pool.map(is_lychrel, range(10000))
    # results = map(is_lychrel, range(10000))
    result = sum(results)
    print(result)


if __name__ == '__main__':
    main()
