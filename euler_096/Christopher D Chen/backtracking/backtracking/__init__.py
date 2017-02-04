#!/usr/bin/env python3
import queue
import sys
if sys.platform in ["win32"]:
    import multiprocess as multiprocessing
    from multiprocess.managers import BaseManager
else:
    import multiprocessing
    from multiprocessing.managers import BaseManager
from queue import LifoQueue
import time
import signal
import copy

class LifoManager(BaseManager):
    def __init__(self,*args,**kwargs):
        signal.signal(signal.SIGINT,signal.SIG_IGN)
        super(LifoManager,self).__init__(*args,**kwargs)
    def start(self, *args, **kwargs):
        super(LifoManager,self).start(*args,**kwargs)


LifoManager.register('LifoQueue', LifoQueue)


class Backtracker():
    """A class that handles backtracking using multiple processes.
    Reflects the API used by the backtracking function itself.
    Given the functions necessary to perform backtracking this class
        """

    def __init__(self, *, next_choice_func =None ,  starting_guesses: list = None, partial_checker=None, candidate_matcher=None):
        """next_choice_func: a function which takes a list (a partial solution) and returns a list of possible next choices.

        starting_guesses: a list of sequences (partial solutions) from which the algorithm should start building.
            Starting guesses may be left as None to delegate that to the next_choice_func.

        partial_checker: a function which takes a partial solution and return whether is still fits within contraints.

        candidate_matcher: a function which returns whether a partial solution has the form of a final solution.
            In the case of solving sudoku, the candidate_matcher might be same as the partial_checker but also 
            checks for the correct length of the solution.
        """

        if None in [next_choice_func, partial_checker]:
            raise ValueError(
                "Backtracking requires both next_choice_func and partial_checker!")
        self.next_choice_func = copy.deepcopy(next_choice_func)
        self.starting_guesses = copy.deepcopy(starting_guesses)
        self.partial_checker = copy.deepcopy(partial_checker)
        self.candidate_matcher = copy.deepcopy(candidate_matcher)
        # instantiate a manager that knows lifo queues
        self.manager = LifoManager()
        self.manager.start()
        self.intermediate_queue = self.manager.LifoQueue()
        self.solutions_queue = self.manager.LifoQueue()
        self.discard_queue = self.manager.LifoQueue()
        # self.intermediate_queue = multiprocessing.Queue()

        # feed in the starting guesses
        for s in starting_guesses:
            for g in next_choice_func(s):
                self.intermediate_queue.put(g)

        self.outboxes = []
        self.children = []

    def go(self, numthreads=1):
        for _ in range(numthreads):
            newbox = queue.Queue()
            self.outboxes.append(newbox)
            self.children.append(
                multiprocessing.Process(
                    target=backtrack,kwargs={
                        "next_choice_func":copy.deepcopy(self.next_choice_func),
                        "partial_checker":self.partial_checker,
                        "candidate_matcher":self.candidate_matcher,
                        "intermediate_queue":self.intermediate_queue,
                        "solutions_queue":self.solutions_queue,
                        "mailbox":newbox,
                        "discard":self.discard_queue
                        }
                )
            )
        for t in self.children:
            t.start()
            # time.sleep(0.1)

    def terminate(self):
        """Terminate all child processes."""
        self.msg_all(1)
        for t in self.children:
            t.terminate()
            t.join()

    def msg_all(self, m):
        """Put a message in mailbox queues of all children."""
        for b in self.outboxes:
            b.put(m)

    def join(self):
        """Wait for all children to complete."""
        for t in self.children:
            t.join()


def worker_wrapper(*args, **kwargs):
    def worker():
        return backtrack(*args, **kwargs)
    return worker


def backtrack(next_choice_func, *, partial_checker=None, candidate_matcher=None,  intermediate_queue=None, solutions_queue=None, mailbox=None, discard=None):
    """next_choice_func should be a function that take a sequences and 
    returns any a list of all possible next items in that sequence.
    candidate_matcher should be a function that returns whether 
    Algorithm:
    Instantiate a queue.
    While it is not empty, pop all of its contents and put all the results
    of the next_choice_func back into the queue.
    Any results of the next_choice_func that match with the candidate_matcher 
    are put in a results queue.
    The algorithm has finished when the queue is empty.
    After that, the results queue is fed out.
    """
    # signal.signal(signal.SIGINT, signal.SIG_IGN)
    paused = False
    if intermediate_queue is None:
        q = multiprocessing.Queue()
    else:
        q = intermediate_queue

    if solutions_queue is None:
        solutions = multiprocessing.Queue()
    else:
        solutions = solutions_queue
    assert not candidate_matcher is None, "A function to match final solutions must be provided."

    while True:
        # quit()
        while not mailbox.empty():
            v = q.get()
            print("Received in inbox:", v)
            if v == 1:
                # return
                quit()
            elif v == 2:
                paused = True
            elif v == 3:
                paused = False
        if not paused:
            try:
                partial = q.get()
                # print(partial)
                # print("partial",partial)
                if candidate_matcher(partial):
                    # print(partial)
                    solutions.put(partial)
                for guess in next_choice_func(partial):
                    if partial_checker(guess):
                        q.put(guess)

                    else:
                        # print("BAD:",partial)
                        if discard:
                            discard.put(guess)
                        pass
                    # print(head)
            except queue.Empty:
                pass
