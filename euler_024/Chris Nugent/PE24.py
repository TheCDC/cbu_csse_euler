import itertools

count = 0
target = 10 ** 6
for p in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    count += 1
    if count == target:
        print(p)
        break