digits = set(range(10))


def generate_pandigitals(current=None, unused=None):
    if not current:
        current = []
    if not unused:
        unused = set(digits)
    if len(unused) == 1:
            # yield a single item list
            # this allows for results to be concatenated
        yield current + [next(iter(unused))]
    else:
        for d in sorted(unused):
            yield from generate_pandigitals(
                current + [d], unused.difference({d}))


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
