import functools

def surprise():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(args):
            print("surprise")
        return wrapper
    return decorator