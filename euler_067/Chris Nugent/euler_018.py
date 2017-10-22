def add_row_to_totals(row_str: str, totals: list) -> list:
    row = parse_row(row_str)
    new_totals = list()
    for i, num in enumerate(totals[1:]):
        new_totals.append(row[i] + max(totals[i], num))
    return new_totals


def parse_row(row: str) -> list:
    return [int(s) for s in row.split()]


def main():
    with open('triangle.txt') as f:
        lines = f.read().strip().split('\n')

    totals = parse_row(lines.pop())
    for line in lines[::-1]:
        totals = add_row_to_totals(line, totals)
    print(totals)


if __name__ == '__main__':
    main()
