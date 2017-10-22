class Wrapper:

    def __init__(self):
        self.to_1 = {1}
        self.to_89 = {89}

    def next_in_chain(number) -> int:
        sum_of_squares = 0
        while number > 0:
            sum_of_squares = sum_of_squares + (number % 10) ** 2
            number = number // 10
        return sum_of_squares

    def make_chain(self, number) -> None:
        chain = {number}
        while True:
            if number in self.to_1:
                self.to_1 |= chain
                return
            elif number in self.to_89:
                self.to_89 |= chain
                return
            else:
                number = Wrapper.next_in_chain(number)
                chain.add(number)


def main():
    w = Wrapper()
    for i in range(1, 10 ** 7):
        w.make_chain(i)
    c = 0
    print(len(w.to_89))


if __name__ == "__main__":
    main()
