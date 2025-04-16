import os
from PIL import Image

def remember_remember(image_path):
    """
    Extracts a hidden message from an image by reading pixel values.
    It looks for pixels with value 1 (black) and uses the y-coordinate to form characters.
    Assumes the image has a message hidden in this way.
    Raises appropriate errors for missing or invalid paths.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        img = Image.open(image_path)
        img = img.convert('L')  # Convert to grayscale
    except Exception as e:
        raise RuntimeError(f"Failed to open or process image: {e}")

    width, height = img.size
    message = []
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if pixel == 1:
                message.append(chr(y))
                break

    return ''.join(message)


if __name__ == '__main__':
    path_to_image = os.path.abspath('./code.png')
    try:
        print(remember_remember(path_to_image))
    except Exception as e:
        print(f"Error: {e}")
