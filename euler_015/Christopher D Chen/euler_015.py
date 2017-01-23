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
    # return [(x + 1 if x + 1 < xbound else x, y), (x, y + 1 if y + 1 < ybound else y)]
    # if x < xbound:

@functools.lru_cache(maxsize=32)
def numPaths(shape, coord=(0, 0)):
    bs = branches(coord, shape)
    # print(len(bs))
    # print(xbound,ybound)
    xbound, ybound = shape
    if len(bs) == 0:
        # print(xbound, ybound)
        # print()
        return 1
    else:
        return sum([numPaths(shape, i) for i in bs])
        # rules


def main():
    xbound = 20
    ybound = 20
    gridWidth = 20
    gridHeight = 20

    # print([numPaths((i,i)) for i in range(15)])
    print(numPaths((gridWidth + 1, gridHeight + 1)))

if __name__ == '__main__':
    main()
