from PIL import Image

img = Image.open('samples/0lqevfyIm54.jpg')
SIZE = 1000, 1000
img = img.resize(SIZE, Image.ANTIALIAS)

CROPPED_WIDTH = 50
CROPPED_HEIGHT = 50


for y in range(0, 1000, CROPPED_HEIGHT):
    for x in range(0, 1000, CROPPED_WIDTH):
        mini_image = img.crop((x, y, x + CROPPED_WIDTH,\
                 y + CROPPED_HEIGHT))


