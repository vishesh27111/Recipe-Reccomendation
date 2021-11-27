# -*- coding: utf-8 -*-
"""yoloV5_DataConverter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S0GqU2HZJaOFt85GMdduOGgXNw290FXs
"""

from google.colab import drive
drive.mount('/content/drive')

! unzip /content/drive/MyDrive/dir.zip -d /content/yolov5

rm -rf /content/drive/MyDrive/obj

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/
!mkdir data
# %cd data
!mkdir images labels
# %cd images 
!mkdir train test
# %cd ..
# %cd labels
!mkdir train test

"hi"

!pip install -U featuretools

import featuretools as ft
ft._version_

'hi'

import os
import glob
import shutil

def remove_ext(list_of_pathnames):
    return [os.path.splitext(filename)[0] for filename in list_of_pathnames]

path = '/content/yolov5/'
os.chdir("/content/yolov5/")   

list_of_jpgs = glob.glob(path+"*.jpg")
list_of_txts = glob.glob(path+"*.txt")

print(list_of_jpgs, "\n\n", list_of_txts) #remove

jpgs_without_extension = remove_ext(list_of_jpgs)
txts_without_extension = remove_ext(list_of_txts)

print(jpgs_without_extension, "\n\n", txts_without_extension) #remove
c = 0
for filename in jpgs_without_extension:
    if filename in txts_without_extension:
        print("moving", filename) #remove
        if c <= len(os.listdir(path))*0.48:
          shutil.copy((filename + '.jpg'), '/content/data/images/train/')
          shutil.copy((filename + '.txt'), '/content/data/labels/train/')
          print("hi from train")

        else:
          shutil.copy((filename + '.jpg'), '/content/data/images/test/')
          shutil.copy((filename + '.txt'), '/content/data/labels/test/')
          print("Hi from test")
        c += 1

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/

! zip -r '/content/drive/MyDrive/yolov5_final_data.zip' 'data'



import os 
len(os.listdir("/content/drive/MyDrive/final_yolov5/"))
