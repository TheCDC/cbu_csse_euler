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


def main():
    g = generate_pandigitals()
    for _ in range(10**6):
        item = next(g)
    print(list_to_num(item, 10))


if __name__ == '__main__':
    main()
