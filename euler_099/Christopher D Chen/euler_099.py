#!/usr/bin/env python3

import math


def val(b, e):
    return e * math.log(b)


def main():
    with open("p099_base_exp.txt") as f:
        lines = f.read().split("\n")
    # lines
    cs = [(index + 1, val(*[int(j) for j in item.split(",")]))
          for index, item in enumerate(lines)]
    # print(cs)
    print(max(cs, key=lambda x: x[1])[0])
    # print(val(2, 3), 2**3)
    # print(val(2, 4), 2**4)

if __name__ == '__main__':
    main()
