from math import log, fabs, ceil, factorial


def heads_for_ratio(ratio, total_flips=1000, threshold=10**9):
    n = log(threshold) - (total_flips * log(1 - ratio))
    d = log(1 + 2 * ratio) - log(1 - ratio)
    return n / d


def estimate(accuracy=10**-20, step=0.05, step_multiplier=-0.1, start=0.01):
    best_ratio = 0
    last_heads = 10 * 999
    best_heads = 10 * 999
    current_ratio = start
    while True:
        current_heads = heads_for_ratio(current_ratio)
        if current_heads < last_heads:
            if current_heads < best_heads:
                best_ratio = current_ratio - step
                best_heads = current_heads
        else:
            step *= step_multiplier
            if fabs(step) < accuracy:
                return ceil(best_heads)
        current_ratio += step
        last_heads = current_heads


def c(left, right):
    a = factorial(left)
    b = factorial(left - right) * factorial(right)
    return a // b


def total_ways(count, total):
    return sum([c(1000, i) for i in range(1000 - 432 + 1)])


if __name__ == '__main__':
    count = estimate()
    prob = total_ways(count, 1000) / (2**1000)
    print('{:.12f}'.format(prob))
