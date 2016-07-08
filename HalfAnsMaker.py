import cv2
import numpy as np
import os
import math

#find red point and create answer
def FindRed(path,new_path,filename):
 img=cv2.imread(path+"/"+filename)
 black_img = np.zeros((256,300,3), np.uint8)
 hight=img.shape[0]
 width=img.shape[1]
 for y in range(hight):
  for x in range(width):
   B = img[y, x, 0]
   G = img[y, x, 1]
   R = img[y, x, 2]
   #find red
   if B<50 and G<50 and R>200:
    halfx=int(math.ceil(x/2))
    halfy=int(math.ceil(y/2))
    #to avoid error
    if halfx>=300: halfx=299
    if halfy>=256: halfy=255
    #input ans in black image
    black_img[halfy, halfx, 0]= 255
    black_img[halfy, halfx, 1]= 255
    black_img[halfy, halfx, 2]= 255
 cv2.imwrite(new_path+"/"+filename, black_img)
 
## main action
img_path = "Ans"
new_path = "ans"
if os.path.isdir(new_path)==False:
 os.mkdir(new_path)    

if(os.path.isdir(img_path)):
 files = os.listdir(img_path)
 for file in files:
  FindRed(img_path,new_path,file)


 
