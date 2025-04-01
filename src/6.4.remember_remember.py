"""
This module provides a function to extract hidden messages from an image by reading pixel values.
It assumes that the message is encoded in the y-coordinate values of black pixels (with value 1).
"""

import os
from PIL import Image

def remember_remember(image_path):
    """
    Extracts a hidden message from an image by reading pixel values.
    It looks for pixels with value 1 (black) and uses the y-coordinate to form characters.
    Assumes the image has a message hidden in this way.
    """
    img = Image.open(image_path)
    img = img.convert('L')  # Convert the image to grayscale
    width, height = img.size
    message = []
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))

            if pixel == 1:  # If the pixel is black
                message.append(chr(y))  # Use the y-coordinate as the ASCII value
                break

    return ''.join(message)


if __name__ == '__main__':
    path_to_image = os.path.abspath('./code.png')  # Renamed variable here
    print(remember_remember(path_to_image))
