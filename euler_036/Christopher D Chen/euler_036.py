from utils import numrepr


def test(i):
    a = bin(i).split('b')[1]
    b = str(i)
    return (b[::-1] == b) and (a == a[::-1])


def main():
    print(numrepr(585, 2))
    s = 0
    for i in range(1000000):
        if test(i):
            print(i)
            s += i
            # print(i)
    print(s)


if __name__ == '__main__':
    main()
