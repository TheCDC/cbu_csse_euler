from math import log, fabs, ceil, factorial


def heads_for_ratio(ratio, total_flips=1000, threshold=10**9):
    """Math that returns number of heads out of total_flips
    needed to have a return ratio equal to threshold"""
    n = log(threshold) - (total_flips * log(1 - ratio))
    d = log(1 + 2 * ratio) - log(1 - ratio)
    return n / d


def combinations(left, right):
    a = factorial(left)
    b = factorial(left - right) * factorial(right)
    return a // b


def estimate(accuracy=10**-20, step=0.05, step_multiplier=-0.1, start=0.01):
    """Use a Newton's-method-like approach to find the optimal
    ratio for surpassing the threshold of 10**9. Returns the
    minimum number of heads needed to surpass the threshhold."""
    # best_ratio = 0
    last_heads = 10 * 999
    best_heads = 10 * 999
    current_ratio = start
    # Continue iterating until within desired accuracy
    while True:
        current_heads = heads_for_ratio(current_ratio, 1000, 10**9)
        if current_heads < last_heads:
            if current_heads < best_heads:
                # best_ratio = current_ratio - step
                best_heads = current_heads
        else:
            step *= step_multiplier
            if fabs(step) < accuracy:
                return ceil(best_heads)
        current_ratio += step
        last_heads = current_heads


def total_ways(count, total):
    """Returns the number of ways that combination
    can produce at least count from total"""
    return sum([combinations(total, i) for i in range(total - count + 1)])


if __name__ == '__main__':
    count_needed = estimate()
    total_flips = 1000
    prob = total_ways(count_needed, total_flips) / (2**total_flips)
    print('{:.12f}'.format(prob))
