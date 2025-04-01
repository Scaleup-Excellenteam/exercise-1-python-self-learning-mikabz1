"""
This module defines a function to extract sequences of at least five consecutive
lowercase letters or exclamation marks ('!') from a binary file ('logo.jpg'),
yielding them when they end with '!' and discarding the trailing '!'.
"""

import os
def parsle_tongue():
    """
       Reads a binary file ('logo.jpg') and extracts sequences of at least five
       consecutive lowercase letters or exclamation marks ('!'), yielding them
       when they end with '!'.
       """
    buffer = ""
    path = os.path.abspath('./logo.jpg')

    try:
        with open(path, 'rb') as file:
            while char := file.read(1):
                char = char.decode('utf-8', errors='ignore')
                if char.islower() or char == '!':
                    buffer += char
                else:buffer = ""
                if  len(buffer) >= 5 and buffer.endswith('!'):
                    yield buffer[:-1]
                    buffer = ""
    except FileNotFoundError:
        print("file not found")

if __name__ == '__main__':
    for message in parsle_tongue():
        print(message)
