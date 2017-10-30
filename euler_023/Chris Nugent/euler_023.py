from utils import divisors


def relevant_abundents(n):
    result = []
    for i in range(1, n):
        if sum(divisors(i)) > i:
            result.append(i)
    return sorted(result)


def main(n=30000):
    print('Finding abundents...')
    abundents = relevant_abundents(n)
    print('Declaring flags...')
    flags = [False for i in range(n + 1)]
    print('Marking flags...')
    for a in abundents:
        for b in abundents:
            if a + b >= n:
                break
            flags[a + b] = True
    print('Flags marked.')
    return sum([x for x in range(n) if not flags[x]])


if __name__ == '__main__':
    print(main())
