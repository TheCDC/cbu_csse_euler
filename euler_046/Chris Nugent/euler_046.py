import math


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num < 0:
        return False
    check = 3
    while check * check <= num:
        if num % check == 0:
            return False
        check += 2
    return True


def is_square(num):
    sqrt = math.sqrt(num)
    return math.floor(sqrt) == sqrt


def main():
    primes = {2}
    number = 3
    while True:
        if is_prime(number):
            primes.add(number)
        else:
            any_true = False
            for p in primes:
                square = (number - p) / 2
                # print('{} - {} = {}'.format(number, p, square))
                if is_square(square):
                    any_true = True
                    break
            if not any_true:
                return number
        number += 2


if __name__ == '__main__':
    n = main()
    print(n)
