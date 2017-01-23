#!/usr/bin/env python3
def main():
	s = str(2**1000)
	n = sum([int(i) for i in s])
	print(n)
if __name__ == '__main__':
	main()