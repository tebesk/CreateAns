import cv2
import numpy as np
import os

img_path = "trn_raw"
new_path = "train"
if os.path.isdir(new_path)==False:
	os.mkdir(new_path)    

if(os.path.isdir(img_path)):
	files = os.listdir(img_path)
	for file in files:
		img = cv2.imread(img_path+"/"+file)
		if not (img == None):
			hight = img.shape[0]
			width = img.shape[1]
			half_img = cv2.resize(img,(hight/2,width/2))
			name, ext = os.path.splitext(file)
			cv2.imwrite(new_path+"/"+name+".bmp", half_img)
		else:
			print 'Not exist'
else:
	print "there is no image folder"

