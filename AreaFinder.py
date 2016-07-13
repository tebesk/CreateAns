# -*- coding: utf-8 -*-
import tensorflow as tf
import cv2
import numpy as np
import os
import math
import time

BASE_PATH = "ans_thresh"
NEWPATH="ans_area"

def OrgorNot(img, x, y):
	B = img[y, x, 0]
	G = img[y, x, 1]
	R = img[y, x, 2]
	if B>10 and G>10 and R>10:
		return 1
	else:
		return 0


def AreaDesigner(img):
	img_area = np.zeros((256,300,3), np.uint8)
	Height, Width = img.shape[:2]
	for y in range(Height):
		right_of_border=0
		for x in range(Width):
			B = img[y, x, 0]
			G = img[y, x, 1]
			R = img[y, x, 2]
			#find red
			if B<50 and G<50 and R>200:
				right_of_border=1
			
			#上、下、右上、右下、右の画素が10以上であれば
			if right_of_border==1:
				if B>10 and G>10 and R>10:
					org =0
					if x<(Width-1):
						org += OrgorNot(img,x+1,y)
						if y>0:
							org += OrgorNot(img,x,y-1)
							org += OrgorNot(img,x+1,y-1)
						if y<(Height-1):
							org += OrgorNot(img,x,y+1)
							org += OrgorNot(img,x+1,y+1)
					if org>0:
						B = img_area[y, x, 0]=255
						G = img_area[y, x, 1]=255
						R = img_area[y, x, 2]=255
			else:
				continue	
	return img_area


if os.path.isdir(NEWPATH)==False:
	os.mkdir(NEWPATH)    
 
if(os.path.isdir(BASE_PATH)):
	files = os.listdir(BASE_PATH)
	
	for file in files:
		img = cv2.imread(BASE_PATH+"/"+file)
		ans_img=AreaDesigner(img)
		cv2.imwrite(NEWPATH+"/"+file, ans_img)


