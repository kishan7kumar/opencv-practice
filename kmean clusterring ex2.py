# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:59:11 2018

@author: kishan
"""

import numpy as np
import cv2
windowname='res2'
cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)
img = cv2.imread('C:\\Users\\kishan\\Pictures\\Goa\\flamenew.jpg')
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 4.0)
K = 8
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow(windowname,res2)
cv2.waitKey(0)
cv2.destroyAllWindows()