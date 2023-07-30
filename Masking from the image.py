# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:26:45 2018

@author: kishan
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1280.jpg'
img = cv2.imread(imgpath,1)
mask = np.zeros(img.shape[:2], np.uint8)
mask[1000:5000, 1000:2000] = 255
masked_img = cv2.bitwise_and(img, img, mask = mask)
plt.imshow(masked_img,'gray')
plt.show()
