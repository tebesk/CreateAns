# -*- coding: utf-8 -*-
import tensorflow as tf
import os
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import PIL
from PIL import Image

IMAGE_WIDTH = 300
IMAGE_HIGHT = 256
IMAGE_PIXELS = IMAGE_WIDTH*IMAGE_HIGHT
NUM_CLASSES = IMAGE_WIDTH*IMAGE_HIGHT

NEWPATH="ans_area_check"
RAWPATH="dns_thresh"
ANSPATH="ans_area"

##回答のラインを引く
#引数（答えがあるフォルダ、
#　　　生データがあるフォルダ、
#　　　新たに答えを入れるフォルダ、
#　　　ファイル名）
def CheckRed(ans_path, raw_path, NEWPATH, filename):
 ans_img=cv2.imread(ans_path+"/"+filename)
 raw_img=cv2.imread(raw_path+"/"+filename)
 for y in range(IMAGE_HIGHT):
  for x in range(IMAGE_WIDTH):
   B = ans_img[y, x, 0]
   G = ans_img[y, x, 1]
   R = ans_img[y, x, 2]
   #find red
   if B>200 and G>200 and R>200:
    #input ans in raw image
    raw_img[y, x, 0]= 0
    raw_img[y, x, 1]= 0
    raw_img[y, x, 2]= 255
 cv2.imwrite(NEWPATH+"/"+filename, raw_img)
 
#file check
Ansfiles = os.listdir(ANSPATH)

#実際の計算　一個ずつファイルを読んでいくことにする
st = time.time()

#folder making
if os.path.isdir(NEWPATH)==False:
	os.mkdir(NEWPATH)

#folder searching
files = os.listdir(ANSPATH)   

#画像を配列の中にぶっこんでいく
for file in files:
	if  os.path.isfile(RAWPATH+"/"+file):
		#image modify
		CheckRed(ANSPATH, RAWPATH, NEWPATH, file)
	else:
		print file
		continue

# change to numpy array
print "***elapsed time %f [sec]" % (time.time() - st)
