def words(n: int) -> str:
    less_than_twenty = dict(enumerate(
        ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]))
    tens = dict(enumerate(["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]))
    s = ''
    if n >= 100:
        s += less_than_twenty[n // 100] + " hundred "
        n %= 100
        if n != 0:
            s += "and "
    if n < 20:
        s += less_than_twenty[n]
    else:
        s += tens[n // 10] + ' ' + less_than_twenty[n % 10]
    return s.strip()

def main():
    total = 0
    for n in range(1, 1000 + 1):
        s = words(n % 1000)
        if n > 999:
            s = words(n // 1000) + " thousand " + s
        total += len(s.replace(" ", ""))
    return total


if __name__ == '__main__':
    print(main())