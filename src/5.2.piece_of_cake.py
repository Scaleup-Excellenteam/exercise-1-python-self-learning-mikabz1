"""
This module provides a function to calculate the weighted sum of values from a dictionary.
It computes the sum based on specific keys and their values, excluding optional keys.
"""
from argparse import ArgumentError


def piece_of_cake(prices:dict , optionals = None , **kwargs ):
    """
       Calculates the weighted sum of values from `dictionary` based on `kwargs`, excluding keys in `optional`.
       Each value in `kwargs` is multiplied by the corresponding value in `dictionary` and divided by 100.
       Returns the total sum of the calculated values.
       """
    try:
        return sum(val / 100 * prices[name] for name , val in kwargs.items() if name not in optionals)
    except KeyError:
        print("KeyError")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    print(piece_of_cake({ 'milk': 8}, chocolate=200, milk=100))
