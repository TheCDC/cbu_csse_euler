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


def main():
    g = generate_pandigitals()
    for i in range(10**6):
        item = next(g)
    print(list_to_num(item, 10))


if __name__ == '__main__':
    main()
