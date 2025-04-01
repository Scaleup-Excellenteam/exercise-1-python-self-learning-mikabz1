from itertools import zip_longest
from typing import Iterable


def interleave(*args:Iterable):
    """Interleave elements from multiple iterables into a list."""
    return [item for items in zip_longest(*args) for item in items if item is not None]

def generator_interleave(*args:Iterable):
    for elem in zip_longest(*args):
        for item in elem:
            if item is not None:
                yield item


if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    for i in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(i , end=",")


