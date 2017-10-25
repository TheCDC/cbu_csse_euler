#!/usr/bin/env python3

"""
Project Euler Problem 14
The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import functools
import multiprocessing as mp


def collatz(n) -> int:
    """The Collatz function."""
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


@functools.lru_cache(maxsize=None)
def seqlen(n) -> int:
    found_length = 0
    while n > 1:
        """Notice a separate Collatz function is not used.
        This is done in order to optimize.
        """
        if n % 2 == 0:
            n = n // 2
        else:
            # the odd case can be optimized
            # odd*3 + 1 will be even, so go ahead and also apply the even case
            n = (3 * n + 1) // 2
            found_length += 1
        found_length += 1
    return found_length + 1


def process_num(n):
    return (n, seqlen(n))


def main():
    pool = mp.Pool()
    results = pool.map(process_num, range(2, 10**6))
    print("{} has the longest chain with {} iterations.".format(
        *max(results, key=lambda t: t[1])))


if __name__ == "__main__":
    main()
