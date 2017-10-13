from collections import deque

def get_pandigitals(current = 0, remaining = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}):
	if not remaining:
		yield current 
	for number in remaining:
		if current == 0 and number == 0:
			continue
		current *= 10
		current += number
		yield from get_pandigitals(current, remaining - {number})
		current //= 10

def check_num(num, start, length, div):
	if start == 8:
		return True
	part = (num // 10 ** (start - 1)) % (10 ** (length))
	if (part % div.pop() == 0):
		return check_num(num, start + 1, length, div)
	else:
		return False

def main():
	sum = 0
	for pandigital in get_pandigitals():
		if check_num(pandigital, 1, 3, [2, 3, 5, 7, 11, 13, 17]):
			sum += pandigital
	print(sum)

if __name__ == "__main__":
	main()