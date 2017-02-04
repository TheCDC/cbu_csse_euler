class Breadcrumb():

    """Used as a marker to de-recurse the list result from backtracking."""

    def __init__(self, depth):
        self.depth = depth

    def __repr__(self):
        return "Breadcrumb({})".format(self.depth)

    def __str__(self):
        return repr(self)


def interpret(l) -> list:
    """Return a list of lists from a list  delineated by Breadcrumb()'s.
    Used to structure the output from backtrack."""
    r = []
    for i in l:
        if isinstance(i, Breadcrumb):
            r.append([])
        else:
            r[-1].append(i)
    # print(r)
    return r


max_depth = -1
def backtrack(guess, next_choice_func,candidate_matcher=None) -> list:
    """Performing backtracking.
    Intermediate guesses are stored in guess. It should usually
    be passed as an empty list, but it may also be used to supply
    a starting guess.
    The next_choice_func should take the guess and return a list 
    possible next choices.

    test_func should return true if a guess is the head of a valid candidate
    for part of a final answer and false otherwise."""
    def bt(guess, next_choice_func, depth,candidate_matcher):
        # print(locals())
        """Wrapped backtracking function that returns 1-dimensional output."""
        tails = []
        next_guesses = []
        for i, c in enumerate(next_choice_func(guess)):

            head = guess + [c]
            # print(head)
            next_guesses.append(head)
        # print(guess, next_guesses)
        for head in next_guesses:
            # print("bt guessing:",head)
            tail = bt(head, next_choice_func, depth=depth + 1,candidate_matcher=candidate_matcher)
            tails.extend([Breadcrumb(depth)] + head + tail)

        # if candidate_matcher:
        #     for t in tails:
        #         if candidate_matcher(t):
        #             return t
        del next_guesses
        del guess
        return tails
        # Interpret deserialzes output.
    return interpret(bt(guess, next_choice_func,  depth=0,candidate_matcher=candidate_matcher))

