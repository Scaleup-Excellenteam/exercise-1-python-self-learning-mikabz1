def long_cat_is_long(text):
    """
    Takes a string of text, removes punctuation, and returns a dictionary with words as keys and their lengths as values.
    Words are processed in lowercase and non-alphabetical characters are discarded.
    """
    words = [''.join(c for c in word if c.isalpha()) for word in text.lower().split()]
    return {word: len(word) for word in words if word}



if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(long_cat_is_long(text))