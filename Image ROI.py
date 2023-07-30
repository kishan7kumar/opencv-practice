# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:08:23 2018

@author: kishan
"""
import cv2
import numpy as np
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1280.jpg'
img = cv2.imread(imgpath,1)
b = img[:,:,2]=0
cv2.namedWindow('pic',cv2.WINDOW_NORMAL)  
cv2.imshow('pic',img)
