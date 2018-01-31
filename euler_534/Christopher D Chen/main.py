import nqueens
import argparse
import time
parser = argparse.ArgumentParser("Generate solutions to the N-Queens problem.")

parser.add_argument(
    'N',
    metavar='N',
    type=int,
    help='The value of N for N-Queens. Board size and number of queens.',
)
parser.add_argument(
    '-w',
    '--weakness',
    default=0,
    type=int,
    help="Weakness factor for Euler 534.",
)

parser.add_argument(
    '-m',
    '--multiprocess',
    default=False,
    help="""Enable multiprocessing.
    Use the parallel version of the algorithm for significant speed gains.
    This produces solutions out of order.""",
    action='store_true',
)

parser.add_argument(
    '--oop',
    default=False,
    help="""Enable the oop representation of solutions.""",
    action='store_true',
)
parser.add_argument(
    '-p',
    '--processes',
    help='Number of processes to execute in parallel.',
    default=8,
    type=int,
    metavar='processes',
)

parser.add_argument(
    '-b',
    '--batch-size',
    help='Size of iteration batches for processes.',
    default=10000,
    type=int,
    metavar='batch_size',
)

parser.add_argument(
    '--print-step',
    help='Size of solutions in between printing.',
    default=1,
    type=int,
    metavar='print_step',
)

parser.add_argument(
    '-q',
    '--quiet',
    help="Suppress all output except the finaly tally.",
    default=False,
    action="store_true",
)

parser.add_argument(
    '-v',
    '--verbose',
    help="Render each solution as ASCII",
    default=False,
    action="store_true",
)


def wrapper(multi, n, weakness, nprocesses, batch, oop=False):
    if multi:

        def wrapped():
            yield from nqueens.generate_solutions_multiprocessed(
                n=n, w=weakness, num_processes=nprocesses, batch_size=batch)
    elif oop:

        def wrapped():
            yield from nqueens.generate_solutions_oop(n=n, w=weakness)
    else:

        def wrapped():
            yield from nqueens.generate_solutions(n=n, w=weakness)

    return wrapped


def main():
    args = parser.parse_args()
    N = args.N
    # print(vars(args))
    # quit()
    algo = wrapper(args.multiprocess, N, args.weakness, args.processes,
                   args.batch_size, args.oop)
    ti = time.time()
    t_start = ti
    c = 0
    try:
        for s in algo():
            tf = time.time()
            if not args.quiet and c % args.print_step == 0:
                print(f"{c}, delta_t={tf-ti:.3f}, t={tf-t_start:.3f}")
                ti = time.time()
                if args.verbose:
                    print(nqueens.render(s, N))
            c += 1
    except KeyboardInterrupt:
        pass
    print(c)


if __name__ == '__main__':
    main()
