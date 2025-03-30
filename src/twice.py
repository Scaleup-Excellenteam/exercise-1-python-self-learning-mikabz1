from decorator import decorator

@decorator
def twice(func, *args, **kwargs):
    func(*args, **kwargs)
    return func(*args, **kwargs)

# Example usage
@twice
def say_hello():
    print("Hello!")

if __name__ == "__main__":
    say_hello()
