# ********** NOISE ON IMAGES ***************

#importing all modules
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1279.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

rows, columns, channels = img1.shape
output = np.zeros(img1.shape,np.uint8)
p = 0.2
for i in range(rows):
    for j in range(columns):
        r = random.random()
        if r<p/2:
            output[i][j] = [0, 0, 0]
        elif r<p:
            output[i][j] = [255,255,255]
        else:
            output[i][j] = img1[i][j]  
            

#displaying output image using matplot library
plt.subplot(1,2,1)
plt.imshow(img1)
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(output)
plt.title('Salt and Pepper Noise')
plt.show()

