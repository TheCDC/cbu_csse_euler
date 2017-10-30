from math import ceil


def divisors(n):
    if n == 2:
        return {1}
    divs = {1}
    for i in range(2, ceil(n**(1 / 2)) + 1):
        if n % i == 0:
            divs.update([i, n // i])
    return divs
