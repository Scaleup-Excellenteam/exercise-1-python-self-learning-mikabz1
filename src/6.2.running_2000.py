import time
from argparse import ArgumentError

def running_2000(func , *args):
    """
    Measures the execution time of a given function using time.perf_counter().
    Handles ArgumentError exceptions and returns 0 in case of failure.
    Usage: running_2000(func, *args) -> execution time in seconds.
    """

    start_time = time.perf_counter()
    try:
        func(*args)
        return time.perf_counter() - start_time
    except ArgumentError:
        print("argument error")
        return 0

if __name__ == '__main__':
    print(running_2000(print, "Hello"))