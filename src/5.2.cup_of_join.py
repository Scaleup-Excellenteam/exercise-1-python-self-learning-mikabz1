def cup_of_join(*args , sep="-"):
    """
       Combines multiple lists into one, inserting a separator between them. Defaults to `"-"` if no separator is provided.
       Returns None if no lists are provided.
       """

    if not args: return None

    result = []
    for i , lst in enumerate(args):
        result.extend(lst)
        if i < len(args) - 1:
            result.append(sep)

    return result

if __name__ == '__main__':
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))
