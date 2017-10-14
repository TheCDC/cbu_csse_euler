digits = set(range(10))


def generate_pandigitals(exclude=frozenset()):
    # get set of unused digits
    remaining = sorted(digits.difference(exclude))
    # base case of only one digit left
    if len(remaining) == 1:
            # yield a single item list
            # this allows for results to be concatenated
        yield [remaining[0]]
    else:
        for d in remaining:
            for i in generate_pandigitals(exclude.union({d})):
                yield [d] + i


def list_to_num(l, b):
    n = 0
    for i in l:
        n = n * b + i
    return n


DIVISORS = [1, 2, 3, 5, 7, 11, 13, 17]


def check_substr_divibility(l):
    for idx, p in reversed(list(enumerate(DIVISORS))):
        n = list_to_num(l[idx:idx + 3], 10)
        if n % p != 0:
            return False
    return True


def main():
    s = 0
    for digit_list in generate_pandigitals():
        if check_substr_divibility(digit_list):
            s += list_to_num(digit_list, 10)
            # print(digit_list)
    print(s)
    # print(i)


if __name__ == '__main__':
    main()
