#!/usr/bin/env python3
import pydot

class Breadcrumb():

    """Used as a marker to de-recurse the list result from backtracking."""

    def __init__(self, depth):
        self.depth = depth

    def __repr__(self):
        return "Breadcrumb({})".format(self.depth)

    def __str__(self):
        return repr(self)


def test(lst, rules) -> bool:
    for rule in rules:
        try:
            if lst.index(rule[1]) < lst.index(rule[0]):
                return False
        except ValueError:
            return True
    return True


def backtrack_old(guess, choice_pool, rules, depth=0) -> list:
    # print(locals())
    def bt(guess, choice_pool, rules, depth):
        tails = []
        for i, c in enumerate(choice_pool):
            head = guess + [c]
            if test(head, rules):
                tail = bt(head,
                          choice_pool[:i] + choice_pool[i + 1:],
                          rules, depth=depth + 1)
                tails.extend([Breadcrumb(depth)] + head + tail)
        return tails
    return interpret(bt(guess, choice_pool, rules, depth))


def backtrack(guess, next_choice_func, test_func, depth=0) -> list:
    # print(locals())
    def bt(guess, next_choice_func, test_func, depth):
        tails = []
        for _, c in enumerate(next_choice_func(guess)):
            head = guess + [c]

            if test_func(head):
                tail = bt(head, next_choice_func, test_func, depth=depth + 1)
                tails.extend([Breadcrumb(depth)] + head + tail)
        return tails
    return interpret(bt(guess, next_choice_func, test_func, depth))


def interpret(l) -> list:
    """Return a list of lists from a list  delineated by Breadcrumb()'s.
    Used to structure the output from backtrack."""
    r = []
    for i in l:
        if isinstance(i, Breadcrumb):
            r.append([])
        else:
            r[-1].extend(i)
    return r


def discard(lst, minset) -> list:
    """Return lst without items that aren't supersets of minset."""
    r = []
    for l in lst:
        if set(l) >= minset:
            r.append(l)
    return r


def get_rules(l) -> list:
    """Return a list of item ordering rules from an iterable."""
    rs = []
    for index, item in enumerate(l):
        for i in range(index):
            rs.append((l[i], item))
    return rs


def main() -> None:
    with open("p079_keylog.txt") as f:
        contents = f.read().strip()
        samples = [tuple(i.strip()) for i in contents.split('\n')]
    all_digits = set(''.join(contents.split('\n')))
    choice_pool = tuple(all_digits)
    orders = []
    for i in samples:
        orders.extend(get_rules(i))
        
    # create and plot the graph of rules
    g = pydot.Dot()
    for o in set(orders):
        e = pydot.Edge(*o)
        g.add_edge(e)
    g.write_png("079_graph.png")
    def my_next_choice(guess):
        """Problem-specific function that return all possible next choices
        from a guess."""
        return tuple(all_digits - set(guess))

    def my_test_func(guess):
        """Problem-specific function that checks if a guess is possible."""
        return test(guess, orders)

    results = backtrack([], my_next_choice, my_test_func)
    for i in [int(''.join(i)) for i in discard(results, all_digits)]:
        print(i, end=" ")
    print()
if __name__ == '__main__':
    main()

