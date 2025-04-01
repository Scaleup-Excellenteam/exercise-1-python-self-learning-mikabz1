"""
This module provides a function to extract hidden messages from an image by reading pixel values.
It assumes that the message is encoded in the y-coordinate values of black pixels (with value 1).
"""

import os
import cv2

def remember_remember(image_path):
    """
    Extracts a hidden message from an image by reading pixel values.
    It looks for pixels with value 1 (black) and uses the y-coordinate to form characters.
    Assumes the image has a message hidden in this way.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read image as grayscale
    width, height = img.shape[1], img.shape[0]  # Get image dimensions (width, height)
    message = []
    for x in range(width):
        for y in range(height):
            pixel = img[y, x]  # Access pixel value (note OpenCV uses y,x indexing)

            if pixel == 0:  # If the pixel is black (grayscale value 0)
                message.append(chr(y))  # Use the y-coordinate as the ASCII value
                break

    return ''.join(message)


if __name__ == '__main__':
    path_to_image = os.path.abspath('./code.png')  # Renamed variable here
    print(remember_remember(path_to_image))
