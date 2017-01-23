from utils import numrepr
def test(n):
	return str(i)[::-1] == str(i) and numrepr(i,2) == numrepr(i,2)[::-1]
i = 0
s = 0
while i < 1000000:
	if test(i):
		s += i
		# print(i)
	i+= 1
print(s)