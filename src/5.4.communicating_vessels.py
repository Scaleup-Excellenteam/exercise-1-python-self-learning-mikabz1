from itertools import chain
from typing import Iterable


def communicating_vessels(*args:Iterable):
    """Interleave elements from multiple iterables into a list."""
    return list(chain.from_iterable(zip(*args)))

def interleave(*args:Iterable):
    for elem in zip(*args):
        yield from elem


if __name__ == '__main__':
    print(communicating_vessels('abc', [1, 2, 3], ('!', '@', '#')))
    for i in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(i , end=",")


