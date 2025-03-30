def group_by(func , iterable):
    """
       Groups elements of an iterable based on the result of applying a given function.
       Returns a dictionary where the keys are the function results, and the values are lists of items.
       Example: group_by(len, ["hi", "bye", "yo", "try"]) returns {2: ['hi', 'yo'], 3: ['bye', 'try']}.
       """
    result = {}
    for item in iterable:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))