"""
This module provides functions for interleaving elements from multiple iterables.
It includes both a list-based function and a generator-based function to achieve this.
"""

from itertools import zip_longest
from typing import Iterable

def interleave(*args: Iterable):
    """
    Interleave elements from multiple iterables into a list.
    
    This function takes multiple iterables as arguments and returns a list
    with the elements from each iterable interleaved. If any iterable is shorter,
    the missing values are ignored.
    """
    return [item for items in zip_longest(*args) for item in items if item is not None]

def generator_interleave(*args: Iterable):
    """
    Interleave elements from multiple iterables into a generator.
    
    This function is similar to `interleave`, but instead of returning a list,
    it yields the elements one at a time, which is memory efficient for large iterables.
    """
    for elem in zip_longest(*args):
        for item in elem:
            if item is not None:
                yield item

if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    for i in generator_interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(i, end=",")
