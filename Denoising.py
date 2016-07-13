# -*- coding: utf-8 -*-
import tensorflow as tf
import cv2
import numpy as np
import os
import math
import time
img_path = "nntrn"
NEWPATH="denoised"

st = time.time()


#画像をMorplogy処理する
def Denoising(path, filename):
	# 4近傍の定義
	#neiborhood4 = np.array([[0, 1, 0],[1, 1, 1],[0, 1, 0]],np.uint8)
	# 8近傍の定義
	neiborhood8 = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]],np.uint8)
	
	img=cv2.imread(path+"/"+filename)
	# 近傍8のオープニング
	img = cv2.morphologyEx(img, cv2.MORPH_OPEN, neiborhood8)
	# 近傍8のクロージング
	img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, neiborhood8)
	return img

#画像の左端を黒くする
def Leftwiper(img, num):
	orgHeight, orgWidth = img.shape[:2]
	for y in range(orgHeight):
		for x in range(num):
			img[y, x, 0]= 0
			img[y, x, 1]= 0
			img[y, x, 2]= 0
	return img

## main action
if os.path.isdir(NEWPATH)==False:
	os.mkdir(NEWPATH)    
 
if(os.path.isdir(img_path)):
	files = os.listdir(img_path)
	
	for file in files:
		img=Denoising(img_path,file)
		#左端を消す
		img = Leftwiper(img,13)
		# save
		cv2.imwrite(NEWPATH+"/"+file, img)

#show cost time
print "***elapsed time %f [sec]" % (time.time() - st)
