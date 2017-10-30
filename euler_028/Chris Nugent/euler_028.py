def count_spiral(n):
    if n % 2 == 0:
        return 0
    total = 1
    top_right = 1
    for ring in range(1, n // 2 + 1):
        # top right behaves by +8n each layer
        top_right += 8 * ring
        # bottom right behaves as TR - 6n
        bottom_right = top_right - (6 * ring)
        # total of corners = 2 * (TR + BR)
        total += 2 * (top_right + bottom_right)
    return total


if __name__ == '__main__':
    print(count_spiral(1001))