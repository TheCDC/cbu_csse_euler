from utils import fib
from math import log,ceil
def nd(n):
	return ceil(log(n)/log(10))
i = 2
a,b = 1,1
while nd(b) < 1000	:
	a,b = b, a+b
	i += 1	
print(i,b,nd(b))

