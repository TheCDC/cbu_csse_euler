def main():
    biggest = 0
    for i in range(101, 1000):
        for j in range(101, 1000):
            if str(i * j) == str(i * j)[::-1] and i * j > biggest:
                biggest = i * j

    print(biggest)

if __name__ == "__main__":
    main()
