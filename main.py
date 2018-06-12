import random
import pickle
import os
import numpy as np
from PIL import Image

def get_gray(img, HEIGHT, WIDTH):
    arr = np.asarray(img)
    HEIGHT = len(arr)
    WIDTH = len(arr[0])
    summation = 0
    for i in range(len(arr)):
        summation += sum(arr[i])/WIDTH

    avg = summation / HEIGHT
    return round(avg, 6)

def compareProximityMid(l, u, mid, gray, arr):
    left = mid - 1
    right = mid + 1
    lVal = 1000000
    rVal = 1000000
    if left >= l:
        lVal = abs(arr[left][0] - gray)
    if right <= u:
        rVal = abs(arr[right][0] - gray)
        
    tmp = abs(arr[mid][0] - gray)

    if tmp <= lVal and tmp <= rVal:
        return True
    return False
    

def get_image_for_gray(gray, height, width, arr):
    mini = 1000000
    comp = 1000000
    file = ''
    '''
    for elem in arr:
        tmp = abs(elem[0] - gray)
        if tmp < comp:
            comp = tmp
            mini = elem[0]
            file = elem[1]
        else:
            continue
    '''
    l = 0
    u = len(arr) - 1
    mid = 0
    while l <= u:
        mid = int((l + u) / 2)
        if compareProximityMid(l, u, mid, gray, arr) == True:
            file = arr[mid][1]
            break
        else:
            if gray < arr[mid][0]:
                u = mid - 1
            else:
                l = mid + 1
    #print('gray', gray, ' got', arr[mid][0])
    return Image.open(file).convert('L').resize((width, height), Image.ANTIALIAS)
        
def create_gray_array(height, width):
    arr = []
    for f in os.listdir('samples/'):
        print('Image:', f)
        tmp = Image.open('samples/'+f).convert('L')\
              .resize((width, height), \
                 Image.ANTIALIAS)
        tmp_gray = get_gray(tmp, height, width)
        arr.append((tmp_gray, 'samples/'+f))
    return sorted(arr, key = lambda x: x[0])

os.system('cls')
print('============== starting code ================')
image_file = 'image.jpg'
output_image = 'new_img' + str(random.randint(0,100000)) + '.jpg'
img = Image.open(image_file).convert('L')
width, height = img.size
SCALING_FACTOR = 5
width = width * SCALING_FACTOR
height = height * SCALING_FACTOR
img = img.resize((width, height), Image.ANTIALIAS)
DIVISION_FACTOR = 300
small_img_width = width // DIVISION_FACTOR
small_img_height = height // DIVISION_FACTOR

new_img = Image.new('L', (width, height))

arr = None
filename = 'pickle'
if(os.path.exists(filename)):
    file = open(filename, 'rb')
    arr = pickle.load(file)
    file.close()
else:
    file = open(filename, 'wb')
    arr = create_gray_array(small_img_height, small_img_width)
    pickle.dump(arr, file)
    file.close()

#print(arr)

_h = height / small_img_height
_w = width / small_img_width
_tot = _h * _w
_tmp = 0
for y in range(0, height, small_img_height):
    for x in range(0, width, small_img_width):
        tmp = img.crop((x, y, x +\
                        small_img_width,\
                        y + small_img_height))
        gray = get_gray(tmp,\
               small_img_width, \
                small_img_height)
        try:
            image = get_image_for_gray(gray,\
                        small_img_height,\
                        small_img_width, arr)
            new_img.paste(image, (x, y))
        except:
            print('exception happended')
            pass
    os.system('cls')
    print(round(_tmp*100/_h, 2), '%')
    _tmp += 1
		

new_img.save(output_image)

