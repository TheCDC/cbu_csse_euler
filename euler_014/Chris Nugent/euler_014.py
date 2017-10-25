from functools import lru_cache
import multiprocessing


@lru_cache(maxsize=None)
def chain_length(value: int) -> int:
    if value == 1:
        return 1
    elif value % 2 == 0:
        return 1 + chain_length(value // 2)
    else:
        return 1 + chain_length(3 * value + 1)


def main():
    pool = multiprocessing.Pool()
    result = pool.map(chain_length, range(1, 10**6))
    print(max(result))


if __name__ == '__main__':
    main()
