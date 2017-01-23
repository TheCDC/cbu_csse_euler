#!/usr/bin/env python3
from utils import numDigits, nthDigit
def ds(n):
    s = 0
    for i in range(numDigits(n)):
        s += nthDigit(n,i)**5
    # print(s)
    return s
def main():
    # find an upper bound of number of digits
    nd = 1
    n = 2
    # find *a* ceiling for numbers that fit the criteria
    while n < ds(n):

        nd += 1
        n = n*10 + 9
    # lower that ceiling until the real one is found
    while n != ds(n):
        n -= 1
    # print("Upper (inclusive):",n)
    # don't include 1
    print(sum([i for i in range(2,n+1) if i == ds(i)]))
if __name__ == '__main__':
    main()