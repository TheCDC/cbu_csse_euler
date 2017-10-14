digits = set(range(10))


def generate_pandigitals(exclude=frozenset()):
    # get set of unused digits
    remaining = digits.difference(exclude)
    for d in sorted(remaining):
        # base case of only one digit left
        if len(remaining) == 1:
            # yield a single item list
            # this allows for results to be concatenated
            # fancy technique for retrieving single item from set
            # without creating new set

            yield [next(iter(remaining))]
        else:
            for i in generate_pandigitals(exclude.union({d})):
                yield [d] + i


def list_to_num(l, b):
    n = 0
    for i in l:
        n = n * b + i
    return n


PRIMES = [2, 3, 5, 7, 11, 13, 17]
INDEX_OFFSET = 1


def check_substr_divibility(l):
    for idx, p in enumerate(PRIMES):
        i = INDEX_OFFSET + idx
        digit_slice = l[i:i + 3]
        n = list_to_num(digit_slice, 10)
        if n % p != 0:
            return False
    return True


def main():
    s = 0
    for n in generate_pandigitals():
        if check_substr_divibility(n):
            s += list_to_num(n, 10)
            # print(n)
    print(s)
    # print(i)


if __name__ == '__main__':
    main()
