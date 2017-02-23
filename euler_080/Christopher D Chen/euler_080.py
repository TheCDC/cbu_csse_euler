import decimal


def decimal_sum(n):
    """Return sum of digits."""
    digits = str(n).replace(".", '')
    s = sum(map(int, digits[:100]))
    return s


def main():
    # ensure that there is enough precision for digits
    decimal.getcontext().prec = 200
    try:
        # validate against the given point
        test_sum = decimal_sum(decimal.Decimal(
            2)**decimal.Decimal(1 / 2))
        assert test_sum == decimal.Decimal(475)
    except AssertionError as e:
        print("Error with validation point: {}".format(test_sum))
        raise e

    mysum = 0
    for i in range(1, 101):
        root = decimal.Decimal(i) ** decimal.Decimal(0.5)
        fractional = (root % decimal.Decimal(1))
        # irrational
        if fractional != 0:
            # print("Root of {} is irrational!".format(i))
            mysum += decimal_sum(fractional)
    print(mysum)


if __name__ == '__main__':
    main()
