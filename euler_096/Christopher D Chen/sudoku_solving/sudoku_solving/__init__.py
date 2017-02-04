#!/usr/bin/env python3
"""Sudoku stuff will be working with a serialized version of a board.
The whole board will be a 1-dimensional list of digits.
Any functions involving a board should be aware of this."""
import sys
sys.path.append('backtracking/')
import backtracking
import time
import os
import signal
import copy
import argparse


class UserRequestedQuit(Exception):
    """Exception to replace KeyboardInterrupt events."""
    pass


class SudokuBoard():

    """Handle a Sudoku board and various bits of information needed to solve it."""

    def __init__(self, serialized, size=9):
        self.size = size
        self.root = int(size**(1 / 2))
        self.square = size * size
        if len(serialized) > size * size:
            raise ValueError("Board too big.")
        elif size < 1:
            raise ValueError("Requested size too small ({})".format(size))
        elif size**(1 / 2) % 1 != 0:
            raise ValueError("Size must be a square number!")
        elif not isinstance(serialized, list):
            raise ValueError("input must be list")
        # assert type(serialized[0]) == int, "Must be list of ints."
        self.original = serialized[:]
        self.serialized = pad_serialized_board(serialized, size)
        self.rows = []
        self.rows = sublists(self.serialized, size)
        self.rownums = list(range(self.size))

    def clone(self):
        """Clone self, a deep copy."""
        other = SudokuBoard(self.serialized[:], self.size)
        other.size = self.size
        other.root = self.root
        other.square = self.square
        other.original = copy.deepcopy(self.original)
        other.serialized = copy.deepcopy(self.serialized)
        other.rows = copy.deepcopy(self.rows)
        other.rownums = copy.deepcopy(self.rownums)
        return other

    def check(self) -> bool:
        """Return whether the board is solved."""
        return (self.next_empty() is None) and self.check_partial()

    def quadrant(self, n) -> list:
        """Return a list of all cells in the nth quadrant, start fomr the top left
        and going first to the right then down."""
        sq = []
        row_offset = self.root * (n // self.root)
        rows = self.rows[row_offset: row_offset + self.root]
        for row in rows:
            col_offset = self.root * (n % self.root)
            sq.extend(row[col_offset: col_offset + self.root])
        return sq

    def get(self, x, y) -> int:
        """Get value of cell at x,y"""
        return self.rows[y][x]

    def set(self, n, x, y):
        self.rows[y][x] = n

    def row(self, y) -> list:
        """Return a list of all cells in the nth row."""
        return self.rows[y]

    def col(self, x) -> list:
        """Return a lsit of all cells in the nth column."""
        return [self.rows[i][x] for i in range(self.size)]

    def check_partial(self) -> bool:
        """Return whether the board does not violate any rules."""
        for i in range(self.size):
            if invalid_set(self.row(i)) or invalid_set(self.col(i)) or invalid_set(self.quadrant(i)):
                # print("invalid row", row)
                return False
        for i in range(self.square):
            # check for any empty cells with 0 candidates
            x, y = lin_to_xy(i, self.size)
            z = self.get(x, y)
            if len(self.candidates(x, y)) == 0 and z == 0:
                return False

        return True

    def candidates(self, x, y) -> set:
        """Get the set of possible digits that could be filled into cell at x,y"""
        cur = self.get(x, y)
        if cur != 0:
            return set([cur])
        ns = []
        # horizontal line
        ns.extend(self.row(y))
        # vertical line
        ns.extend(self.col(x))
        xmin = self.root * (x // self.root)
        xmax = xmin + self.root
        ymin = self.root * (y // self.root)
        ymax = ymin + self.root
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                ns.append(self.rows[y][x])
        # ns.extend(self.rows[y][x] for x in range(xmin, xmax) for y in
        # range(ymin, ymax)  )

        return all_digits(self.size) - set(ns) - set([0])

    def next_empty(self) -> tuple:
        """Return xy coords of next empty cell, None if there are none."""
        for index, r in enumerate(self.rows):
            try:
                return (r.index(0), index)
            except ValueError:
                pass
        return None
        # raise ValueError("No empty spaces on board.")

    def populate(self,max_depth=1) -> int:
        """Fill in all the freebies.
        Returns the number of freebies filled in."""
        if max_depth == 0:
            max_depth = -1
        outsum = 0
        while max_depth != 0:
            count = 0
            for x in range(self.size):
                for y in range(self.size):
                    cur = self.get(x, y)
                    if cur == 0:
                        cs = self.candidates(x, y)
                        if len(cs) == 1:
                            self.set(cs.pop(), x, y)
                            count += 1
            outsum += count
            max_depth -= 1
            if count == 0:
                break

        return outsum

    def optimize(self) -> None:
        """Transform the board such that knowns are concentrated in the top left.
        Keep track of original shape of the board with self.rownums

        Sort the rows of quadrants in descending order weighted by the number of knowns/row.
        """
        outrows = []
        outrownums = []
        sorted_quad_rows = []
        for qrownum, quad_rows in enumerate(sublists(self.rows, self.root)):
            offset = qrownum * self.root
            zipped = list(zip(quad_rows, self.rownums[
                          offset:offset + self.root]))
            zipped.sort(key=lambda x: weight_row(x[0]), reverse=True)
            sorted_quad_rows.append(
                (zipped, max(weight_row(i[0]) for i in zipped)))
        sorted_quad_rows.sort(key=lambda x: x[1], reverse=True)
        for qrow in sorted_quad_rows:
            for row in qrow[0]:
                outrows.append(row[0])
                outrownums.append(row[1])
        self.rows = outrows
        self.rownums = outrownums

    def optimized(self):
        """Return optimized copy of self."""
        new = self.clone()
        new.optimize()
        return new

    def unoptimize(self) -> None:
        """Sort self.rows by self.rownums."""
        zipped = list(zip(self.rows, self.rownums))
        zipped.sort(key=lambda x: x[1])
        self.rows = [i[0] for i in zipped]
        self.rownums = [i[1] for i in zipped]

    def unoptimized(self):
        """Return untransformed copy of self."""
        new = self.clone()
        new.unoptimize()
        return new

    def __repr__(self) -> str:
        rs = []
        _ = [rs.extend(r) for r in self.rows]
        return "SudokuBoard({}, {})".format(rs, self.size)

    def __str__(self) -> str:
        sroot = int(self.size**(1 / 2))
        rowsep = "-" * (self.size + self.size // self.root + 1)
        return rowsep + "\n" + ('\n').join("|" + ''.join((str(i) if i != 0 else "-") + " " * (len(str(self.size)) - len(str(i))) + "|" * ((index + 1) % sroot == 0) for index, i in enumerate(row)) + ("\n" + rowsep) * ((irow + 1) % sroot == 0) for irow, row in enumerate(self.rows))

    def serialize(self):
        return ''.join(''.join([str(col) for col in row]) for row in self.rows)


def weight_row(r):
    """Higher rating is better.
    Measure how closely information is packed towards the beginning of a row.
    Used when transforming a board to optimize backtracking."""

    continuous = 0
    for _ in r:
        if r != 0:
            continuous += 1
        else:
            break
    return sum((i != 0) / (index + 1) for index, i in enumerate(r)) / len(r)


def all_digits(size):
    """Return all possible digits of a board of a given size."""
    return set(range(1, size + 1))


def lin_to_xy(n, size) -> tuple:
    """Get xy coords of linear position starting at top left
    and going right and down."""
    return (n % size, n // size)


def sublists(l, partition_size) -> list:
    """Return list of lists.
    l partitioned lists of length equal to partition_size."""
    return [l[i:i + partition_size] for i in range(0, len(l), partition_size)]


def pad_serialized_board(head, size) -> tuple:
    return head + [0 for i in range((size * size) - len(head))]


def invalid_set(x) -> bool:
    nozeroes = len([i for i in x if i != 0])
    try:
        uniques = len(set(x) - set([0]))
    except Exception as e:
        print("Error checking if invalid:", x)
        raise e
    return uniques < nozeroes


def sudoku_next_choices(board) -> list:
    """Return next legal permutaions of a board.
    Used for backtracking."""
    out = []
    try:
        x, y = board.next_empty()
    except TypeError:
        # no spaces found
        return []
    # print(x,y)
    for c in board.candidates(x, y):
        # print(c,x,y)
        b = board.clone()
        b.set(c, x, y)
        # print(b)
        b.optimize()
        b.populate(max_depth=0)
        out.append(b)
        # print("Set",x,y,"to",c)
    return out


def sudoku_final_test(board):
    """Return whether a board is completed."""
    return board.check()


def sudoku_partial_test(board):
    """Return whether a board is still legal."""
    return board.check_partial()


def board_from_string(s, size=9):
    l = []
    if size <= 9:
        l = list(map(int, s))
    else:
        l = [int(i) if len(i) > 0 else 0 for i in s.split('.')]
    return SudokuBoard(l, size)


def solve_sudoku(board, *, num_processes=4, timeout=10):
    if not board.check_partial():
        raise ValueError("Ilegal starting board.")
    br = backtracking.Backtracker(
        next_choice_func=sudoku_next_choices,
        candidate_matcher=sudoku_final_test,
        partial_checker=sudoku_partial_test,
        starting_guesses=[board])
    br.go(numthreads=num_processes)
    ti = time.time()
    while br.solutions_queue.empty():
        if timeout:
            if time.time() - ti >= timeout:
                return None
    br.terminate()
    br.join()
    if not br.solutions_queue.empty():
        return br.solutions_queue.get().unoptimized()
    else:
        return None


def solve_string(s, *args, size=9, **kwargs) -> SudokuBoard:
    """Take a string serialized board return the solved board.
    Results may vary based on threading and race conditions."""
    if size <= 9:
        return solve_list([int(i) for i in s], *args, size, **kwargs)
    else:
        return solve_list([int(i) if len(i) > 0 else 0 for i in s.split('.')],
                          size,
                          **kwargs
                          )


def solve_list(l, size=9, *args, **kwargs) -> SudokuBoard:
    """Take a list serialized board and return the solved board.
    Results may vary based on threading."""
    return solve_sudoku(SudokuBoard(l, size), *args, **kwargs)


def quit_handler(a, b):
    print("Caught Ctrl-C")
    raise UserRequestedQuit()




def main():
    parser = argparse.ArgumentParser(
        description="Solve Sudoku puzzles with logic and multiprocessed backtracking.")
    parser.add_argument("board",nargs="?", metavar="BOARD",
                        help="Serialized board, read from top left to right. Use '.' for empty cell.", type=str)
    parser.add_argument(
        "-s", metavar="Board size. Must be a square number.", type=int, default=9)
    parser.add_argument("-p", metavar="Number of processes.", type=int, default=4)
    parser.add_argument("--flat", action='store_const', const=True)
    parser.add_argument("--debug", action='store_const', const=True)
    parser.add_argument("--show", help="Pretty print the board before solving.",
                        action='store_const', const=True)
    cmdargs = parser.parse_args()
    if cmdargs.debug:
        print("ARGS:", cmdargs)
    if cmdargs.board:
        try:
            b = board_from_string(cmdargs.board, cmdargs.s)
            if cmdargs.show:
                print(b)
            solution = solve_sudoku(b, num_processes=cmdargs.p)
            if cmdargs.flat:
                print(solution.serialize())
            else:
                print(solution)

            quit()
        except Exception as e:
            raise e
    if sys.platform == "linux":
        os.setpgrp()
    print("Sudoku")
    print("Test case:")
    some_boards = [
        "000050040200800530510029678000004003072030950600200000125940087098003002060080000",
        "483921657900305001001806400008102900700000008006708200002609500800203009005010300",
        "000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "900100400007020080060000000400500200080090010003006000100700030005008900020000006",
        "003020600900305001001806400008102900700000008006708200002609500800203009005010300",
        "800000000003600000070090200050007000000045700000100030001000068008500010090000400",
    ]
    cases = [list(map(
        int, i)) for i in some_boards]

    # start = []
    bsize = 9
    # print(start)
    tb = SudokuBoard(cases[-1], bsize)
    print(tb)
    assert tb.check_partial(), "Test input failure"
    numthreads = 4
    try:
        while True:
            numthreads = int(
                input("How many processes? default=4\n>>>").strip())
            if numthreads > 32:
                input("Are you sure you want {} processes?".format(numthreads))
            else:
                break
    except ValueError:
        pass
    except EOFError:
        quit()
    print(numthreads, "process(es)")
    ti_solve = time.time()
    br = backtracking.Backtracker(
        next_choice_func=sudoku_next_choices,
        candidate_matcher=sudoku_final_test,
        partial_checker=sudoku_partial_test,
        starting_guesses=[tb])
    br.go(numthreads=numthreads)

    while br.solutions_queue.empty():
        pass
    br.terminate()
    br.join()
    if not br.solutions_queue.empty():
        print("Solution found!")
        print("DeltaT = {:.5f}ish".format(time.time() - ti_solve), "seconds")
        results = []
        while not br.solutions_queue.empty():
            r = br.solutions_queue.get()
            r.unoptimize()
            print(r)
            results.append(r)
        results = [i for i in results if i.check()]
        # with open("solutions.txt", 'w') as f:
        #     f.write("{} boards\n".format(len(results)) +
        #             '\n'.join(str(i) for i in results))

    # discarded = []
    # while not br.discard_queue.empty():
    #     discarded.append(str(br.discard_queue.get().untransformed()))
    # with open("discarded.txt", 'w') as f:
    #     f.write("{} discarded\n".format(len(discarded)) + '\n'.join(discarded))


if __name__ == '__main__':
    main()
