from utils import primeFactors

found = []

i = 1
while len(found) < 4:
	i+= 1
	if len(set(primeFactors(i))) == 4:
		found.append(i)
	else:
		found = []

print(found[0])