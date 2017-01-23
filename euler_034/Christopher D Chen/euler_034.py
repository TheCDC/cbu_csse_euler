#!/usr/bin/env python3
from utils import fact, numDigits, nthDigit

def dfsum(n):
    s = 0
    for i in range(numDigits(n,10)):
        s += fact(nthDigit(n,i,10))
    return s

def test(n):
    return dfsum(n) == n

def main():
    print(test(145))
    # find an upper bound on num of digits
    d = 9
    n = d
    while dfsum(n) >= n:
        n = n*10 + d
    print(n)
    mysum = 0
    while n > 0:
        if test(n):
            mysum += n 
        n -= 1
        if n%(100000) == 0:
            print(n)
    print(mysum)


if __name__ == '__main__':
    main()