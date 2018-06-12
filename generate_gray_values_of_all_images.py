import os
import numpy as np
from PIL import Image

def get_gray(img, HEIGHT, WIDTH):
    arr = np.asarray(img)

    summation = 0
    for i in range(HEIGHT):
        summation += sum(arr[i])/WIDTH

    avg = summation // HEIGHT
    return avg


HEIGHT = 50
WIDTH = 50
SIZE = HEIGHT, WIDTH

FOLDER = 'samples/'
files = [ FOLDER + f for f in os.listdir(FOLDER) ]

for f in files:
    img = Image.open(f).convert('L').resize(SIZE, Image.ANTIALIAS)
    print(get_gray(img, HEIGHT, WIDTH))
