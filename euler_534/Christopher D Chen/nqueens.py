import multiprocessing
import os
from enum import Enum


class Sentinel(Enum):
    STACK_END = 0


class QueensPartialSolution:
    def __init__(self, n, w, filled_spaces=None, queens=None, num_queens=None):
        self.n = n
        self.w = w
        self.limit = n - 1 - w
        self.numbers = set(range(n))
        if filled_spaces is not None:
            self.filled_spaces = filled_spaces
        else:
            self.filled_spaces = [set() for _ in range(n)]

        if queens is not None:
            self.queens = queens
        else:
            self.queens = [None for _ in range(n)]

        if num_queens is not None:
            self.num_queens = num_queens
        else:
            self.num_queens = 0

    def next_placements(self):
        """Generates args for place_queen."""
        for x in self.numbers - self.filled_spaces[self.num_queens]:
            yield dict(x=x, y=self.num_queens)

    def place_queen(self, x, y):
        if x in self.filled_spaces[y]:
            return False
        if self.queens[y] is None:
            self.num_queens += 1
        self.queens[y] = x

        start = (y - self.limit)
        if start < 0:
            start = 0

        stop = y + self.limit + 1
        if stop > len(self.filled_spaces):
            stop = len(self.filled_spaces)

        for y_existing in range(start, stop, 1):

            xdiff = y_existing - y
            if xdiff < 0:
                xdiff = -xdiff

            if xdiff > self.limit:
                return True
            col = self.filled_spaces[y_existing].copy()
            col.update([x, x + xdiff, x - xdiff])
            self.filled_spaces[y_existing] = col
        self.filled_spaces[y] = self.numbers

        return True

    def copy(self):
        qps = QueensPartialSolution(
            self.n,
            self.w,
            filled_spaces=self.filled_spaces[:],
            queens=self.queens[:],
            num_queens=self.num_queens)
        return qps

    def __str__(self):
        lines = [
            f'{index}|' + ' '.join(map(str, sorted(bag)))
            for index, bag in enumerate(self.filled_spaces)
        ]
        lines.append('=' * len(lines[-1]))
        return '\n'.join(lines)


def generate_next_partials(partial: "List[int]" = None, n: int = 8,
                           w: int = 0):
    if partial is None:
        partial = list()
    if len(partial) < n:
        for i in get_safe_pos_list(partial, n, w):
            p = partial + [i]
            yield p
        # for i in range(n):
        #     p = partial + [i]
        #     if check_newest(p, n, w):
        #         yield p


def generate_next_partials_oop(partial: QueensPartialSolution = None,
                               n: int = 8,
                               w: int = 0):
    if partial is None:
        partial = QueensPartialSolution(n, w)
    nq = partial.num_queens
    if nq < partial.n:
        original = partial
        for coords in original.next_placements():
            new_p = original.copy()
            new_p.place_queen(**coords)
            yield new_p


def get_safe_pos_list(state, n, w):
    safe_pos_list = [True for i in range(n)]
    k = len(state)
    limit = n - 1 - w
    # for index in range(max(0, k - limit), k):
    for index in range(k):
        if k - index >= n - w:
            continue
        j = state[index]
        safe_pos_list[j] = False
        h = k - index + j
        if h >= 0 and h < n:
            safe_pos_list[h] = False
        h = index - k + j
        if h >= 0 and h < n:
            safe_pos_list[h] = False
    for index, item in enumerate(safe_pos_list):
        if item:
            yield index


def is_valid(l: "List[int]") -> bool:
    for a in range(len(l)):
        ai = l[a]
        for b in range(a + 1, len(l)):
            bi = l[b]
            # check diagonal and horizontal
            # difference between rows
            x = a - b
            # difference between columns
            y = ai - bi
            # do two comparisons instead of one with abs
            # for performance
            if y == x or y == -x or ai == bi:
                return False

    return True


def check_newest(psol: "List[int]", n: int, w: int) -> bool:
    """A fast partial solution checker.
    It's O(n) because it assumes that only the newly placed
    piece could possibly be in error.
    """
    limit = n - 1 - w
    y = len(psol) - 1
    x = psol[y]
    # only have to iterate as far back as the range of a queen (inclusive)
    # for y2 in range(y):
    for y2 in range(max(y - limit, 0), y):
        x2 = psol[y2]
        xdiff = x2 - x  # may be positive or negative
        ydiff = y - y2  # always positive
        if xdiff == 0 and ydiff <= limit:
            return False
        if xdiff == ydiff or xdiff == -ydiff:
            # use ydiff because it's always positive
            if ydiff <= limit:
                return False
    return True


def is_final_oop(p: QueensPartialSolution) -> bool:
    if p.num_queens == p.n:
        # print('oop final:', p)
        return True
    else:
        return False


def is_final(l, n) -> bool:
    return len(l) == n


def render(l: "List[int]", n: int) -> str:
    line = ['-'] * n
    out = list()
    for i in l:
        buf = line[:]
        buf[i] = 'x'
        out.append(' '.join(buf))
    out.append('=' * len(out[-1]))
    return '\n'.join(out)


def generate_solutions(n=8, w=0, print_step=None):
    N = n
    queue = list()
    # prefill
    for x in generate_next_partials(n=n, w=w):
        queue.append(x)
    step = 0
    while len(queue) > 0:
        if print_step:
            if step % print_step == 0:
                print(step)
        step += 1
        x = queue.pop()
        if is_final(x, N):
            yield x
        else:
            for xx in generate_next_partials(x, N, w):
                queue.append(xx)


def generate_solutions_oop(n=8, w=0, print_step=None):
    N = n
    queue = list()
    # prefill
    queue.extend(generate_next_partials_oop(partial=None, n=n, w=w))
    step = 0
    while len(queue) > 0:
        if print_step:
            if step % print_step == 0:
                print(step)
        step += 1
        x = queue.pop()
        if is_final_oop(x):
            yield x
        else:
            queue.extend(generate_next_partials_oop(x, N, w))


def worker(n, w, batch_size, inqueue, outqueue):
    """Multiprocessing worker."""
    internal_queue = list()
    while True:

        p = inqueue.pop()

        if p is Sentinel.STACK_END:
            # print("quitting")
            outqueue.put(Sentinel.STACK_END)
            return
        internal_queue.append(p)
        # ========== Batches ==========
        # perform a batch of iterations before returning results
        # to the main queue
        # a larger batch size leads to greater memory usage
        for _ in range(batch_size):
            if len(internal_queue) == 0:
                # print("break")
                break
            # apply the backtracking algo
            sub_partial = internal_queue.pop()
            if is_final(sub_partial, n):
                outqueue.put(sub_partial)
            else:
                for next_partial in generate_next_partials(sub_partial, n, w):
                    internal_queue.append(next_partial)

        while len(internal_queue) > 0:
            x = internal_queue.pop()
            inqueue.append(x)


def generate_solutions_multiprocessed(n=8,
                                      w=0,
                                      num_processes=os.cpu_count(),
                                      batch_size=1000):
    num_workers = num_processes
    # instantiate a manager to manage a list
    # a list is necessary in order to have a LIFO queue
    with multiprocessing.Manager() as manager:

        partials_queue = manager.list()
        solutions_queue = manager.Queue()
        # prefill
        for _ in range(num_workers):
            partials_queue.append(Sentinel.STACK_END)
        for x in generate_next_partials([], n):
            partials_queue.append(x)
        # spawn and start workers
        workers = []
        for _ in range(num_workers):
            worker_process = multiprocessing.Process(
                target=worker,
                args=(n, w, batch_size, partials_queue, solutions_queue))
            workers.append(worker_process)
        for worker_process in workers:
            worker_process.start()
        # yield from the queue until all worker have exited
        found_exit_codes = 0
        while found_exit_codes < num_workers:
            s = solutions_queue.get()
            if s is Sentinel.STACK_END:
                found_exit_codes += 1
            else:
                yield s
        for worker_process in workers:
            worker_process.join()
