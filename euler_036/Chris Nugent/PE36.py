def check_number(n):
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])


def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


def main():
    limit = 10**6
    total = 0
    for i in range(limit):
        if check_number(i):
            total += i
    return total


if __name__ == '__main__':
    print(main())