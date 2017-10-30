def main(amax, bmax):
    distinct = set()
    for a in range(2, amax + 1):
        distinct.update([a**b for b in range(2, bmax + 1)])
    return len(distinct)

if __name__ == '__main__':
    print(main(100, 100))