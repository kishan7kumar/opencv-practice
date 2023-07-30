# GEOMETRIC TRANSFORMATION OR AFFINE TRANSFORMATION ON IMAGES

#importing all modules
import cv2
import matplotlib.pyplot as plt
import numpy as np

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1279.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

rows, columns, channels = img1.shape
T = np.float32([[1, 0, 450],[0, 1, 450]])
print(T)
output = cv2.warpAffine(img1, T, (columns, rows))

#displaying output image using matplot library
plt.imshow(output)
plt.title('shifted output')
plt.show()
