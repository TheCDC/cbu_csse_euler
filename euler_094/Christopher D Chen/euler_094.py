#!/usr/bin/env python3


def perimeter(t):
    return sum(t)


def almosts(n):
    return [(n, n, n + 1), (n, n, n - 1)]


def main():
    s = 0
    n = 0
    while True:
        for i in almosts(n):
            if perimeter(i) < 1000000000:
                s += perimeter(i)
            else:
                break
    print(s)

if __name__ == '__main__':
    main()
