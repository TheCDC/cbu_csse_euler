from decimal import Decimal
from math import floor


def ds(n):
    s = 0
    for i in range(100):
        s += floor((Decimal(n * 10**(i + 1))**Decimal(0.5)) % 10)
    return s


def main():
    print(ds(2))
if __name__ == '__main__':
    main()
