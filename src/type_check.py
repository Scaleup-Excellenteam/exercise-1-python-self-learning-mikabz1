import functools

class TypeCheckError(Exception):
    """Custom exception for type mismatch errors."""
    pass

def type_check(correct_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(args):
            if not isinstance(args, correct_type):
                raise TypeCheckError
            return func(args)
        return wrapper
    return decorator

