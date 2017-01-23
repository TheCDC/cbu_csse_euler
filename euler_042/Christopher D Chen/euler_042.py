#!/usr/bin/env python3

from euler_045 import nt


def encode(word):
    return sum(ord(c) - 83 + 19 for c in word)


def test(word):
    encoded = encode(word)
    r = nt(encoded)
    return r == int(r)


def main():
    # print(encode("SKY"))
    with open("p042_words.txt") as f:
        words = f.read().replace('"', '').replace(" ", '').split(",")
    # print(words[:10])
    mysum = 0
    for word in words:
        if test(word):
            mysum += 1
    print(mysum)
if __name__ == '__main__':
    main()
