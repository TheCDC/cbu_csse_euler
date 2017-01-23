from itertools import permutations

g = permutations(list(range(10))[::-1])

i = 0
for p in g:
	if i == 1000000:
		break
	else:
		pass
print(p)