def main():
    fibs = [0, 1]
    while fibs[-1] < 4000000:
        fibs.append(fibs[-1] + fibs[-2])
    while fibs[-1] > 4000000:
        fibs.pop()
    print(sum([i for i in fibs if i % 2 == 0]))


if __name__ == '__main__':
    main()
