from math import factorial


def magic(x: int, y: int) -> int:
    return factorial(x + y) // (factorial(x) * factorial(y))


if __name__ == '__main__':
    print(magic(20, 20))
