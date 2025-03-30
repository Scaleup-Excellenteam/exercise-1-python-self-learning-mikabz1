import os
from PIL import Image

def remember_remember(path):
    
    img = Image.open(path)
    img = img.convert('L')
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
    path = os.path.abspath('./code.png')
    print(remember_remember(path))