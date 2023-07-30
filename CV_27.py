# ROTATING IMAGES

#importing all modules
import cv2
import matplotlib.pyplot as plt


#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1279.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

rows, columns, channels = img1.shape
R = cv2.getRotationMatrix2D((columns/2, rows/2),90,1)
output = cv2.warpAffine(img1, R, (columns, rows))

#displaying output image using matplot library
plt.imshow(output)
plt.title('shifted output')
plt.show()
