
digits = set(range(10))


def generate_pandigitals(exclude=None):
    # get set of unused digits
    if not exclude:
        exclude = set()
    remaining = digits.difference(exclude)
    for d in sorted(remaining):
        if len(remaining) == 1:
            # yield a single item list
            # this allows for results to be concatenated
            yield [set(remaining).pop()]
        else:
            for i in generate_pandigitals(exclude.union({d})):
                yield [d] + i


primes = [2, 3, 5, 7, 11, 13, 17]
digit_index_offset = 1


def list_to_num(l, b):
    n = 0
    for i in l:
        n = n * b + i
    return n


def check_substr_divibility(l):
    for idx, p in enumerate(primes):
        i = digit_index_offset + idx
        digit_slice = l[i:i + 3]
        n = list_to_num(digit_slice, 10)
        if n % p != 0:
            return False
    return True


def main():
    s = 0
    print(next(generate_pandigitals()))
    for n in generate_pandigitals():
        if check_substr_divibility(n):
            s += list_to_num(n, 10)
            # print(n)
    print(s)
    # print(i)


if __name__ == '__main__':
    main()
