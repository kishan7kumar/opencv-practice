# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:58:29 2018

@author: kishan kumar
"""
#importing all modules
import cv2
import matplotlib.pyplot as plt
#import numpy as np

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\Goa\\'
imgpath1 = imgpath + 'flamenew.jpg'

#reading images in  grayscale 
img1 = cv2.imread(imgpath1,0)
#img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

'''Laplacian logic'''
edges_laplace = cv2.Laplacian(img1, -1, ksize=5, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT)

'''Scharr logic 1'''
#edgesx = cv2.Scharr(img1, cv2.CV_64F,0,1)
#edgesy = cv2.Scharr(img1, cv2.CV_64F,1,0)
#edges_scharr = edgesx + edgesy

'''Scharr logic 2'''
edgesx = cv2.Scharr(img1, -1,dx=0, dy=1, scale= 1,delta=0, borderType=cv2.BORDER_DEFAULT) 
edgesy = cv2.Scharr(img1, -1,dx=1, dy=0, scale= 1,delta=0, borderType=cv2.BORDER_DEFAULT) 
edges_scharr = edgesx + edgesy

'''Sobel logic 1'''
#edgesx = cv2.Sobel(img1, -1, dx=0, dy=1, ksize=5, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
#edgesy = cv2.Sobel(img1, -1, dx=1, dy=0, ksize=5, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
#edges_sobel = edgesx + edgesy

'''Sobel Logic 2'''
#edgesx = cv2.Scharr(img1, cv2.CV_64F,0,1,ksize = 5)
#edgesy = cv2.Scharr(img1, cv2.CV_64F,1,0, ksize = 5)
#edges_sobel = edgesx + edgesy

'''Sobel Logic 3'''
#sobelx8u = cv2.Sobel(img1,cv2.CV_8U,0,1,ksize = 5)
#sobelx64f = cv2.Sobel(img1, cv2.CV_64F,0,1,ksize= 5)
#abs_sobel64f = np.absolute(sobelx64f)
#sobel_8u = np.uint8(abs_sobel64f)

#displaying output image using matplot library
plt.subplot(3,2,1)
plt.imshow(img1, cmap = 'gray')
plt.title('Original grayscale image')
plt.xticks([])
plt.yticks([])

plt.subplot(3,2,2)
plt.imshow(edges_laplace, cmap = 'gray')
plt.title('Laplace output image')
plt.xticks([])
plt.yticks([])

plt.subplot(3,2,3)
plt.imshow(edgesx, cmap = 'gray')
plt.title('Horizontal lines detection output image')
#plt.imshow(sobelx8u, cmap = 'gray')
#plt.title('Sobel CV_8u output image')
plt.xticks([])
plt.yticks([])

plt.subplot(3,2,4)
plt.imshow(edgesy, cmap = 'gray')
plt.title('Vertical line detecion output image')
#plt.imshow(sobel_8u, cmap = 'gray')
#plt.title('Sobel abs(CV_64f) output image')
plt.xticks([])
plt.yticks([])

plt.subplot(3,2,5)
plt.imshow(edges_scharr, cmap = 'gray')
plt.title('Sobel X+Y output image')
plt.xticks([])
plt.yticks([])


plt.show()
