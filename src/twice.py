"""
This module defines a decorator `twice` that calls a function twice when it is decorated.
"""

from decorator import decorator

@decorator
def twice(func, *args, **kwargs):
    """
    A decorator that calls the decorated function twice.

    :param func: The function to be decorated.
    :param args: Arguments passed to the decorated function.
    :param kwargs: Keyword arguments passed to the decorated function.
    :return: The result of the second function call.
    """
    func(*args, **kwargs)
    return func(*args, **kwargs)

# Example usage
@twice
def say_hello():
    """
    Prints a hello message.
    """
    print("Hello!")

if __name__ == "__main__":
    say_hello()
