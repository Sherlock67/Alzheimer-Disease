import os

folder1Dir = os.listdir('D:\CSE DOCUMENT\Image Processing\Data\Moving')
folder2Dir = os.listdir('D:\CSE DOCUMENT\Image Processing\Data\Dataset')

for file in folder2Dir:
    if file in folder1Dir:
        os.remove(os.path.join('D:\CSE DOCUMENT\Image Processing\Data\Moving', file))
