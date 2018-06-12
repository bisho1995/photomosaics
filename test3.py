import numpy as np
from PIL import Image

def get_gray(img, HEIGHT, WIDTH):
    arr = np.asarray(img)

    summation = 0
    for i in range(HEIGHT):
        summation += sum(arr[i])/WIDTH

    avg = summation / HEIGHT
    return avg

img = Image.open('samples/0lqevfyIm54.jpg')
HEIGHT = 50
WIDTH = 50
img = img.convert('L').resize((50, 50), Image.ANTIALIAS)


print(get_gray(img, HEIGHT, WIDTH))




