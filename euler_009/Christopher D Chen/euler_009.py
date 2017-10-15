#!/usr/bin/env python3


def main():
    SUM = 1000
    for c in range(1, SUM):
        for a in range(1, SUM - c):
            b = SUM - a - c
            if a**2 + b**2 == c**2:
                # print(a,b,c,a*b*c)
                # print(a,b,c)
                print(a * b * c)
                return


if __name__ == '__main__':
    main()
