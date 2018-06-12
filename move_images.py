import os
import random
def move_file(folder):
    for f in os.listdir(folder):
        if os.path.isfile(folder + f):
            os.rename(folder + f,'samples/'+ str(random.randint(0,10000000)) + f)

output = 'samples'
inputPath = 'samples/101_ObjectCategories/'
folders = [inputPath + f + '/' for f in os.listdir(inputPath)\
           if os.path.isdir(inputPath + f)]

for folder in folders:
    move_file(folder)    
