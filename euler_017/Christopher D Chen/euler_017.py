#!/usr/bin/env python3

"""
Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.

"""
from utils import numDigits, nthDigit
def words(n):
	s = ''
	underTwenty =dict(enumerate(["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]))
	tens = dict(enumerate(["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]))
	if n >= 100:
		s+= underTwenty[nthDigit(n,2,10)] + ' hundred'
		if n % 100:
			s += " and "
	if n%100 < 20 and n%100 > 0:

		s+= underTwenty[n%100]
	else:
		s += tens[nthDigit(n,1,10)] + ' ' + (underTwenty[n%10] if n%10 > 0 else '')
		pass

	return s
	# d = {0:}
	suffix = ''
	prefix = ''
	for exponent in range(numDigits(n,10)):
		if exponent ==0:
			pass
def main():
	print([words(i) for i in range(1,110)])
	print(words(331).replace(' ',''))
	print(sum([len(words(i).replace(' ','')) for i in range(1,1000+1)]))
if __name__ == '__main__':
	main()