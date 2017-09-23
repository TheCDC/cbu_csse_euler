def digits(n):
    if n == 0:
        return [0]
    ds = []
    while n > 0:
        ds.append(n % 10)
        n = n // 10
    return list(reversed(ds))


def permuted(n):
    """Return the sum of each digit squared."""
    return sum(d**2 for d in digits(n))


def main():
    # set of terminators
    targets = {1, 89}
    # create a structure to remember what numbers terminate where
    results = {
        t: {t} for t in targets
    }
    MAX = 10 * 10**6
    num_added = 0
    for i in range(1, MAX):
        n = i
        while True:
            # find which terminating numbers this number has previously been
            # found to reach
            matches = [t for t in results.keys() if n in results[t]]
            assert len(matches) < 2
            # if any terminators match, add this number to the corresponding
            # set
            if len(matches) > 0:
                results[matches[0]].add(i)
                num_added += 1
                break
            # if the number has not yet terminated, permute is
            n = permuted(n)
    print(len(results[89]))
    print(num_added)


if __name__ == '__main__':
    main()
