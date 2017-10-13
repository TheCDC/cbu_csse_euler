from collections import deque

sum = 0

def iterate_nums(current, remaining):
	if current > 10 ** 9:
		if check_num(current, 1, 3, deque([2, 3, 5, 7, 11, 13, 17])):
			global sum
			sum += current

	for number in remaining:
		if current == 0 and number == 0:
			continue
		current *= 10
		current += number
		iterate_nums(current, remaining - {number})
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
	numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	iterate_nums(0, numbers)
	print(sum)

if __name__ == "__main__":
	main()