import cv2
import numpy as np
import os
import math

#find red point and create answer
def FindBlueHalfIMG(img):
 black_img = np.zeros((256,300,3), np.uint8)
 
 hight=img.shape[0]
 width=img.shape[1]
 
 for y in range(hight):
  check_blue =0 
  min_x=-1
  max_x=-1
  
  for x in range(width):
   B = img[y, x, 0]
   G = img[y, x, 1]
   R = img[y, x, 2]
       
   if B>200 and G<50 and R<50:
    check_blue=check_blue+1
   
    if check_blue == 1:
     min_x = x
     max_x = x
    if check_blue >1:
     max_x = x
  
  for x in range(width):
   if x>= min_x and x<=max_x:
    halfx=int(math.ceil(x/2))
    halfy=int(math.ceil(y/2))
    #to avoid error
    if halfx>=300: halfx=299
    if halfy>=256: halfy=255
    #input ans in black image
    black_img[halfy, halfx, 0]= 255
    black_img[halfy, halfx, 1]= 0
    black_img[halfy, halfx, 2]= 0    
 
 return black_img

def FindBlue(img):
 black_img = np.zeros((512,600,3), np.uint8)
 
 hight=img.shape[0]
 width=img.shape[1]
 
 for y in range(hight):
  check_blue =0 
  min_x=-1
  max_x=-1
  
  for x in range(width):
   B = img[y, x, 0]
   G = img[y, x, 1]
   R = img[y, x, 2]
       
   if B>200 and G<50 and R<50:
    check_blue=check_blue+1
   
    if check_blue == 1:
     min_x = x
     max_x = x
    if check_blue >1:
     max_x = x
  
  for x in range(width):
   if x>= min_x and x<=max_x:
    #input ans in black image
    black_img[y, x, 0]= 255
    black_img[y, x, 1]= 0
    black_img[y, x, 2]= 0    
 
 return black_img

 
## main action
img_path = "Ando_Edited/andou_modified_160914150823.BMP"
new_path = "IMG2BMP/160914150823.IMG/BlueOnly"
halfnew_path = "IMG2BMP/160914150823.IMG/halfBlueOnlyPNG"

if os.path.isdir(new_path)==False:
 os.mkdir(new_path)    
if os.path.isdir(halfnew_path)==False:
 os.mkdir(halfnew_path)    

if(os.path.isdir(img_path)):
 files = os.listdir(img_path)
 for file in files:
  img = cv2.imread(img_path+"/"+file)
  normal_img = FindBlue(img)
  half_img = FindBlueHalfIMG(img)
  cv2.imwrite(new_path+"/"+file, normal_img)
  cv2.imwrite(halfnew_path+"/"+file+".png", half_img)


 
