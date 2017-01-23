def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)
def main():
	print(sum([int(i) for i in str(fact(100))]))
if __name__ == '__main__':
	main()