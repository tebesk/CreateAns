# -*- coding: utf-8 -*-
import tensorflow as tf
import cv2
import numpy as np
import os
import math
import time

PATH = "denoised"
NEWPATH="dns_thresh"

st = time.time()

if os.path.isdir(NEWPATH)==False:
	os.mkdir(NEWPATH)    
 
if(os.path.isdir(PATH)):
	files = os.listdir(PATH)
	
	for file in files:
		img = cv2.imread(PATH+"/"+file)
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ret,thresh = cv2.threshold(img_gray,30,255,cv2.THRESH_TOZERO)
		cv2.imwrite(NEWPATH+"/"+file, thresh)

#show cost time
print "***elapsed time %f [sec]" % (time.time() - st)
