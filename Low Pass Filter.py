# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:09:36 2018

@author: kishan kumar
"""
#importing all modules
import cv2
import matplotlib.pyplot as plt
#import numpy as np

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1338.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

#applying low pass filter operation
box = cv2.boxFilter(img1,-1, (53, 53))
blur = cv2.blur(img1,(13,13))
gaussian = cv2.GaussianBlur(img1,(17,17),0)

#displaying output image using matplot library
plt.subplot(2,2,1)
plt.imshow(img1)
plt.title('Original image')
plt.xticks([]) 
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(box)
plt.title('Box blur image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(blur)
plt.title('Normal blur image')
plt.xticks([])
plt.yticks([])
plt.subplot(2,2,4)

plt.imshow(gaussian)
plt.title('gaussian blur image(smoothing)')
plt.xticks([])
plt.yticks([])

plt.show()