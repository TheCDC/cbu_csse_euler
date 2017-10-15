#!/usr/bin/env python3
def num_rect_positions(w, h, bw, bh):
    return (bw - w + 1) * (bh - h + 1)


def rect_sum(x, y):
    return x * y * (1 + x) * (1 + y) // 4


def main():
    N = 2000000
    i = 1
    while rect_sum(1, i) < 2000000:
        i += 1
    tests = sorted([(j, rect_sum(1, j)) for j in range(i - 100, i + 100)],
                   key=lambda x: 1 / abs(N - x[-1]))
    boundary = tests[-1][0]
    # print(boundary)

    closest = ((0, 0), 0)

    for x in range(1, int(boundary**(1 / 2)) + 1):
        for y in range(1, boundary + 1):
            if abs(rect_sum(x, y) - N) < abs(closest[1] - N):
                closest = ((x, y), rect_sum(x, y))

    # print(closest)
    print(closest[0][0] * closest[0][1])


if __name__ == '__main__':
    main()
