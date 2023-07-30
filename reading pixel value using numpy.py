# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:49:25 2018

@author: kishan kumar
"""

import cv2

imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1280.jpg'
img = cv2.imread(imgpath,1)
c = img.item(100,100,2)
print(c)