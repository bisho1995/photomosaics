import sys
from PIL import Image

FOLDER = 'samples/'
image_names = [ FOLDER + '0lqevfyIm54.jpg',\
                FOLDER + '1DAqhek_0qI.jpg',\
                FOLDER + '1HmtbpxZ5aI.jpg' ]
images = list(map(Image.open, image_names))
SIZE = 128, 128
images = [i.convert('L').resize(SIZE, Image.ANTIALIAS)\
          for i in images]

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
total_height = max(heights)

new_img = Image.new('RGB', (total_width, total_height))

x_offset = 0
y_offset = 0
for im in images:
    new_img.paste(im, (x_offset, y_offset))
    x_offset += im.size[0]

new_img.save('new_img.jpg')
