"""
This module defines a decorator function `surprise` that wraps functions and prints "surprise" when the wrapped function is called.
"""

import functools

def surprise():
    """
    A decorator that wraps a function and prints 'surprise' when it is called.

    :return: The decorator function that wraps the target function.
    :rtype: function
    """
    def decorator(func):
        """
        The actual decorator function that wraps a function.

        :param func: The function to be decorated.
        :return: The wrapper function that prints 'surprise'.
        :rtype: function
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            The wrapper function that adds behavior before calling the original function.

            :param args: Arguments passed to the wrapped function.
            :param kwargs: Keyword arguments passed to the wrapped function.
            """
            print("surprise")
            return func(*args, **kwargs)
        return wrapper
    return decorator
