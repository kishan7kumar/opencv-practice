import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading image and changing colorspace as required
imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest Image\\1.jpg'
bgr_image = cv2.imread(imgpath1,1)
rgb_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)

#thresholding operation
ret, thresh = cv2.threshold(gray_image,40,60,cv2.THRESH_BINARY_INV )

#defining kernel for morphological operations
kernel = np.ones((7,7),np.uint8)

#eroding for getting the background clear
sure_bg = cv2.erode(thresh, kernel, iterations  = 5)      #sure background

#making the foreground
dilation = cv2.dilate(sure_bg, kernel ,iterations = 14)   #sure foreground
dilation2 = np.uint8(dilation)
unknown = cv2.subtract(sure_bg,dilation2)               #unknown region

#image segmentation
ret, markers = cv2.connectedComponents(dilation2)
markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(rgb_image,markers)
rgb_image[markers == 1] = [255,0,0]

#displaying all outputs
plt.subplot(3,3,1)
plt.imshow(thresh, cmap = 'gray')
plt.title('thresholding')

plt.subplot(3,3,2)
plt.imshow(sure_bg, cmap = 'gray')
plt.title('erosion')

plt.subplot(3,3,3)
plt.imshow(dilation2, cmap = 'gray')
plt.title('dilation')

plt.subplot(3,3,4)
plt.imshow(markers)    #plt.imshow(gray_image, cmap = 'gray')
plt.title('segmented image')

plt.subplot(3,3,5)
plt.imshow(rgb_image)    #plt.imshow(gray_image, cmap = 'gray')
plt.title('output image')



plt.show()