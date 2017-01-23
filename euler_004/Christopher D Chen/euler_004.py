big = 0

for first in range(100,1000):
	for second in range(100,1000):
		product = first*second
		if str(product) == str(product)[::-1]:
			if product > big:
				big = product
				# print(big)

print(big)
# print(max([i for i in range(100,100**2) if str(i) == str(i)[::-1]]))