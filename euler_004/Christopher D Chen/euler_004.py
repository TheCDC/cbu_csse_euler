#!/usr/bin/env python3
def generate_numbers():
    for first in range(100, 1000):
        for second in range(100, 1000):
            product = first * second
            yield product


def main():
    big = 0
    for product in generate_numbers():
        if str(product) == str(product)[::-1]:
            if product > big:
                big = product
                # print(big)

    print(big)
    # print(max([i for i in range(100,100**2) if str(i) == str(i)[::-1]]))


if __name__ == '__main__':
    main()
