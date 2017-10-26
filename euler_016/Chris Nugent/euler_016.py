def digits(num):
    while num > 0:
        yield num % 10
        num //= 10

if __name__ == '__main__':
    total = sum(list(digits(2**1000)))
    print(total)
