def main():
    a, b = 1, 1
    count = 2
    while len(str(b)) < 1000:
        a, b = b, a + b
        count += 1

    print(count)

if __name__ == "__main__":
    main()
