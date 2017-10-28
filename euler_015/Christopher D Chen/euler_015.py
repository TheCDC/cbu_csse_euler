#!/usr/bin/env python3

import functools


def branches(coord, shape):
    bs = []
    # print(coord)
    x, y = coord
    xbound, ybound = shape
    if x + 1 < xbound:
        bs.append((x + 1, y))
    if y + 1 < ybound:
        bs.append((x, y + 1))
    return bs


@functools.lru_cache(maxsize=None)
def numPaths(shape, coord=(0, 0)):
    bs = branches(coord, shape)
    if len(bs) == 0:
        return 1
    else:
        return sum([numPaths(shape, i) for i in bs])


def main():
    gridWidth = 20
    gridHeight = 20

    print(numPaths((gridWidth + 1, gridHeight + 1)))


if __name__ == '__main__':
    main()
