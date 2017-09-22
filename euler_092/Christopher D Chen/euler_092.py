def digits(n):
    if n == 0:
        return [0]
    ds = []
    while n > 0:
        ds.append(n % 10)
        n = n // 10
    return list(reversed(ds))


def permuted(n):
    return sum(d**2 for d in digits(n))


def main():
    targets = {1, 89}
    results = {
        t: {t} for t in targets
    }
    MAX = 10 * 10**6
    for i in range(1, MAX):
        if i % (MAX // 10) == 0:
            print(i / MAX)
        n = i
        while True:
            matches = [t for t in results.keys() if n in results[t]]
            if len(matches) > 0:
                results[matches[0]].add(i)
                break
            n = permuted(n)
    print(len(results[89]))


if __name__ == '__main__':
    main()
