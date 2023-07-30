# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:02:01 2018

@author: kishan kumar
"""
#importing all modules
import cv2
import matplotlib.pyplot as plt
import numpy as np

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1279.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

#change the value of matrix for different effects
k = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1 ]), np.float32)
output = cv2.filter2D(img1,-1, k)

#displaying output image using matplot library
plt.subplot(1,2,1)
plt.imshow(img1)
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(output)
plt.title('Kernel image')

plt.show()
