"""
This module defines a decorator `type_check` that checks if the arguments passed to a function 
match the expected type. If the type mismatch occurs, it raises a `TypeCheckError`.
"""

import functools

class TypeCheckError(Exception):
    """Custom exception for type mismatch errors."""

def type_check(correct_type):
    """
    A decorator that checks if the argument passed to the function matches the expected type.

    :param correct_type: The type that the argument should match.
    :type correct_type: type
    :return: The decorator function that wraps the target function.
    :rtype: function
    """
    def decorator(func):
        """
        The actual decorator function that wraps a function and checks the argument type.

        :param func: The function to be decorated.
        :return: The wrapper function that performs type checking.
        :rtype: function
        """
        @functools.wraps(func)
        def wrapper(args):
            """
            The wrapper function that checks the argument type before calling the original function.

            :param args: The argument passed to the wrapped function.
            """
            if not isinstance(args, correct_type):
                raise TypeCheckError(f"Argument must be of type {correct_type}")
            return func(args)
        return wrapper
    return decorator
