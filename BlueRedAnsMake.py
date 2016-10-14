import cv2
import numpy as np
import os
import math

#find red point and create answer
def RedBlueHalfIMG(red_img,blue_img):

	black_img = np.zeros((256,300,3), np.uint8)
	hight=red_img.shape[0]
	width=red_img.shape[1]
	for y in range(hight):
		for x in range(width):
			redB = red_img[y, x, 0]
			redG = red_img[y, x, 1]
			redR = red_img[y, x, 2]			
			blueB = blue_img[y, x, 0]
			blueG = blue_img[y, x, 1]
			blueR = blue_img[y, x, 2]
			
			if redB>200 and redG>200 and redR>200:
				black_img[y, x, 0]= 0
				black_img[y, x, 1]= 0
				black_img[y, x, 2]= 255
			
			if blueB>200 and blueG<50 and blueR<50:
				black_img[y, x, 0]= 255
				black_img[y, x, 1]= 0
				black_img[y, x, 2]= 0
	
				
	return black_img

## main action
path ="IMG2BMP/160914150823.IMG"
red_path =  path + "/Ans"
blue_path = path + "/halfBlueOnly"
new_path =  path + "/RBans"

if os.path.isdir(new_path)==False:
	os.mkdir(new_path)    

if(os.path.isdir(red_path)):
	files = os.listdir(red_path)

for file in files:
	red_img = cv2.imread(red_path+"/"+file)
	blue_img = cv2.imread(blue_path+"/"+file)
	
	img = RedBlueHalfIMG(red_img, blue_img)
	
	cv2.imwrite(new_path+"/"+file, img)
