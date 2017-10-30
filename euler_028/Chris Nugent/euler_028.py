def count_spiral(n):
    # Time for math :(
    # top right behaves as
    # 01  09  25  49
    #   08  16  24
    #     08  08
    #       00
    #
    # f(0) = 1 = c
    #        c = 1
    # f(1) = 9 = a + b + 1
    #        a + b = 8
    # f(2) = 25 = 4a + 2b + 1
    #        4a + 2b = 24
    #        2a = 8
    #        a = 4
    #        b = 4
    #        c = 1
    # f(x) = 4x**2 + 4x + 1
    # bottom right behaves as
    # 01  03  13  31
    #   02  10  18
    #     08  08
    #       00
    #
    # g(0) = 1 = c
    # g(1) = 3 = a + b + 1
    #        2 = a + b
    # g(2) = 13 = 4a + 2b + 1
    #        4a + 2b = 12
    #        2a = 8
    #        a = 4
    #        b = -2
    # g(x) = 4x**2 - 2x + 1
    # 
    # h(x) = f(x) + g(x) = 8x**2 + 2x + 2
    # sum = 2 * h(x) + 1 (for center)
    n //= 2
    total = 0
    total += 8 * n * (n + 1) * (2 * n + 1) // 6
    total += 2 * n * (n + 1) // 2
    total += 2 * n
    total = 2 * total + 1
    return total


if __name__ == '__main__':
    print(count_spiral(1001))