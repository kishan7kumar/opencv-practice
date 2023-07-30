# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 13:09:26 2018

@author: kishan kumar
"""
import cv2

imgpath = 'C:\\Users\\kishan\\Pictures\\Goa\\flamenew.jpg'
img = cv2.imread(imgpath,0)
cv2.imshow('hello',img)




