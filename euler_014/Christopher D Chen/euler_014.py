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


@functools.lru_cache(maxsize=4096*2)
def collatz(n) -> int:
    return (n // 2)*((n+1)%2) + (3 * n + 1)*(n%2)

seq_dict = dict()

def seqlen(n) -> int:
    nn = n
    l = 0
    while n > 1:
        try:
            return l + seq_dict[n]
        except KeyError:
            pass
        c = collatz(n)
        n=c
        l += 1
    l += 1
    seq_dict.update({n:l})
    # print(nn,l)
    return l


def main():
        # print(seqlen(13))
        # print(seqlen(100))
        # print(seqlen(10000))

    longest = 0
    N = 0
    for i in range(2,1000000):
        n = seqlen(i)
        if n > longest:
            longest = n
            N = i
    # results = [(i,seqlen(i)) for i in range(2, 1000000)]
    # with open("014.txt",'w') as f:
    #     f.write('\n'.join(results))
    print(N)

if __name__ == "__main__":
    main()
