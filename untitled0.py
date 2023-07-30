# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:16:22 2018

@author: kishan
"""

import cv2

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\Goa\\'
imgpath1 = imgpath + 'IMG_0598.jpg'

#reading images in  grayscale 
img1 = cv2.imread(imgpath1)

cv2.imshow('hello',img1)