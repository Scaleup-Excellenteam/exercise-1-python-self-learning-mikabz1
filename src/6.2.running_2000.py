"""
This module provides a decorator-like function, running_2000, which measures
the execution time of a given function using time.perf_counter(). It also handles
ArgumentError exceptions and returns 0 in case of failure.
"""

import time
from argparse import ArgumentError

def running_2000(func, *args, **kwargs):
    """
    Measures the execution time of a given function using time.perf_counter().
    Handles ArgumentError exceptions and returns 0 in case of failure.
    Usage: running_2000(func, *args) -> execution time in seconds.
    """

    start_time = time.perf_counter()
    try:
        func(*args, **kwargs)
        return time.perf_counter() - start_time
    except ArgumentError:
        print("argument error")
        return 0

if __name__ == '__main__':
    print(running_2000(print, "Hello"))
