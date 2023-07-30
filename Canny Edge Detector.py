
import cv2
import matplotlib.pyplot as plt
#import numpy as np

#importing image from folder
imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest1.jpg'


#reading images in  grayscale 
img1 = cv2.imread(imgpath1,0)

#img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
L1 = cv2.Canny(img1, 227 ,214, L2gradient =False)
L2 = cv2.Canny(img1, 50, 250, apertureSize = 5, L2gradient = True)

#displaying output image using matplot library
plt.subplot(1,3,1)
plt.imshow(img1, cmap = 'gray')
plt.title('Original grayscale image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2)
plt.imshow(L1, cmap = 'gray')
plt.title('L1 form')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.imshow(L2 ,cmap = 'gray')
plt.title('L2 form')
plt.xticks([])
plt.yticks([])

plt.show()
