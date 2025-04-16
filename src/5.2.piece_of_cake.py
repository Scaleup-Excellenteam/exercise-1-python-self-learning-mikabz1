def piece_of_cake(prices: dict, optionals=None, **kwargs):
    """
    Calculates the weighted sum of values from `prices` based on `kwargs`,
    excluding keys in `optionals`.
    Each value in `kwargs` is multiplied by the corresponding value in `prices` and divided by 100.
    Returns the total sum of the calculated values.
    """
    if optionals is None:
        optionals = []

    try:
        return sum(val / 100 * prices[name] for name, val in kwargs.items() if name not in optionals)
    except KeyError:
        print("KeyError")
        return None

if __name__ == '__main__':
    print(piece_of_cake({'milk': 8}, chocolate=200, milk=100))  # Output: 8.0
