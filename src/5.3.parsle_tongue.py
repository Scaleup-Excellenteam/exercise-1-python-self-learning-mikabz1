
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
                    yield buffer
                    buffer = ""
    except FileNotFoundError:
        return

if __name__ == '__main__':
    for message in parsle_tongue():
        print(message)