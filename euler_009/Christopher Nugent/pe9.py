def main():
    z = 1000
    for a in range(1, z):
        for c in range(1, z - a):
            b = z - a - c
            # sum of a,b,c is now 1000
            # validate pythagorean triple
            if a**2 + b**2 == c**2:
                print(a*b*c)
                return


if __name__ == "__main__":
    main()
