# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:41:41 2018

@author: kishan kumar
"""
#importing all modules
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\Goa\\'
imgpath1 = imgpath + 'IMG_0604.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

#creating noisy image using Salt and Pepper Noise method
rows, columns, channels = img1.shape
noise_img = np.zeros(img1.shape, np.uint8)
p = 0.05
for i in range(rows):
    for j in range(columns):
        r = random.random()
        if r<p/2:
            noise_img[i][j] = [0, 0, 0]
        elif r<p:
            noise_img[i][j] = [255,255,255]
        else:
            noise_img[i][j] = img1[i][j]  
            
#denoise the noisy image using medianblur function
denoise_img = cv2.medianBlur(noise_img,3)

#displaying output image using matplot library
plt.subplot(1,3,1)
plt.imshow(img1)
plt.title('Original image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2)
plt.imshow(noise_img)
plt.title('Salt and Pepper Noise image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.imshow(denoise_img)
plt.title('Median blur or denoised image')
plt.xticks([])
plt.yticks([])

plt.show()
