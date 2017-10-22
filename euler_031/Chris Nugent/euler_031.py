from functools import lru_cache


@lru_cache(maxsize=None)
def count_solutions(coins: tuple, n: int, money: int) -> int:
    # There is exactly one way to represent 0 cents: the empty set
    if money == 0:
        return 1
    # Cannot represent negative money or without coins
    elif money < 0 or n < 1:
        return 0
    # Sum solutions including this coin and not including this coin
    return count_solutions(coins, n - 1, money) + \
        count_solutions(coins, n, money - coins[n - 1])


def main():
    coins = tuple([1, 2, 5, 10, 20, 50, 100, 200])
    money = 200  # $2.00
    count = count_solutions(coins, len(coins), money)
    print(count)


if __name__ == "__main__":
    main()
