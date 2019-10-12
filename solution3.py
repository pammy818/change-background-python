import cv2
import numpy as np

#step1:compressed image size
image=cv2.imread('greenscreen.jpg') #read the picture
background=cv2.imread('hongkong.jpg')
rows,cols,channels=background.shape #read the shape of hongkong.jpg
background=cv2.resize(background,None,fx=0.7,fy=0.7)#resize background
rows,cols,channels=image.shape #read the shape of greenscreen
image=cv2.resize(image,None,fx=0.3,fy=0.3)#resize greenscreen
cv2.imshow('img',image)#show greenscreen which has been resized

rows,cols,channels = image.shape#rows，cols最后一定要是前景图片的，后面遍历图片需要用到

#step2: convert hsv
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#step3: get mask
low_green=np.array([33,100,0])
up_green=np.array([150,255,100])

#replace
center=[141,70]
for i in range(rows):
    for j in range(cols):
        if all(image[i,j] >= low_green) and all(image[i,j]<= up_green):
            background[center[0]+i,center[1]+j]=background[center[0]+i,center[1]+j]
        else:
                background[center[0]+i,center[1]+j]=image[i,j]
 
cv2.imshow('now',background)

cv2.waitKey(0)