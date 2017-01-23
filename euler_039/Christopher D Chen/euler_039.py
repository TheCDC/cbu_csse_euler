from functools import lru_cache

@lru_cache(maxsize=1000)
def test(a,b,c):
	return a**2 + b**2 == c**2

@lru_cache(maxsize=1000)
def num_solutions(n):
	ns = 0
	for a in range(1,n+1):
		for b in range(1,a):
			if (a**2 + b**2)**(1/2) % 1 == 0:
				c = n-a-b
				if test(a, b, c):
					# print(n,a,b,c,n%4==0)
					ns += 1
				
	return ns
def solutions(n):
	for a in range(1,n+1):
		for b in range(1,a):
			c = n-a-b
			if test(a, b, c):
				yield (n,a,b,c)
N = 1000

assert num_solutions(120) == 3

pmax = 0
biggest = num_solutions(1000)
for i in range(1000,0,-2):
	a = num_solutions(i)
	if a > biggest:
		# print("New biggest:",a,"at i =",i)
		biggest = a
		pmax = i
print(pmax)
# ss = [num_solutions(i) for i in range(1000,0,-1)]
