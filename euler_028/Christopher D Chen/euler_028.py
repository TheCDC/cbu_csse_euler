def corner_sum(n):
    """Math"""
    if n == 0:
        return 1
    elif n > 0:
        return 16 * n**2 + 4 * n + 4


def super_sum(n):
    return sum(corner_sum(i) for i in range(n + 1))


def main():
    # print(corner_sum(2))
    print(super_sum((1001 - 1) // 2))


if __name__ == '__main__':
    main()
