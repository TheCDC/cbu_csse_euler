known = set()
for a in range(2,100+1):
	for b in range(2,100+1):
		known.update({a**b})
# print(known)
print(len(known))