from functools import lru_cache
import multiprocessing


@lru_cache(maxsize=None)
def chain_length(value: int) -> int:
    if value == 1:
        return 1
    elif value % 2 == 0:
        return 1 + chain_length(value // 2)
    else:
        return 2 + chain_length((3 * value + 1) // 2)

def process_num(value: int) -> (int, int):
	#print(chain_length.cache_info())
	return (value, chain_length(value))

def main():
    pool = multiprocessing.Pool()
    result = pool.map(process_num, range(1, 10**6))
    print(max(result, key=lambda t:t[1]))


if __name__ == '__main__':
    main()
