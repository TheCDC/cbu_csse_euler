with open("p022_names.txt") as f:
    contents = f.read()
names = sorted([i.strip('"') for i in contents.split(',')])


def score(s):
    return sum([ord(i) - 65 + 1 for i in s])

# print(names[:10])

print(sum(score(item)*(index+1) for index, item in enumerate(names)))
