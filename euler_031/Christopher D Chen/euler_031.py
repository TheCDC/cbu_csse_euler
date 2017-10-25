#!/usr/bin/env python3
from functools import lru_cache


@lru_cache(maxsize=None)
def count_configurations(coins: list, current: int, cutoff: int=None):
    # print(current, cutoff)
    if cutoff is None:
        cutoff = len(coins) - 1
    if current == 0:
        return 1
    elif cutoff < 0 or current <= 0:
        return 0
    else:
        return count_configurations(coins, current, cutoff - 1)\
            + count_configurations(coins, current - coins[cutoff], cutoff)\



def main():
    coins = tuple(sorted([1, 2, 5, 10, 20, 50, 100, 200]))
    print(count_configurations(coins, 200))

    # uncomment if you dare
    # try:
    #     for amount in range(1, 1000000 + 1, 1):
    #         print(amount, count_configurations(coins, amount))
    # except RecursionError:
    #     print("ERROR")
    # print(count_configurations.cache_info())


if __name__ == '__main__':
    main()
