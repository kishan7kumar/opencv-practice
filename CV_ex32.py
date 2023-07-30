# ************** ADAPTIVE THRESHOLDING OF IMAGES ********

#importing all modules
import cv2
import matplotlib.pyplot as plt

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1339.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,0)
#img11 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)


block_size = 507
constant = 10
th1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, block_size, constant)
th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, constant) 

output = [img1, th1, th2]
titles = ['Original image', 'Mean Adaptive', 'Gaussian Adaptive']

#creating a normal sized window
plt.subplot(1,3,1)
plt.imshow(output[0], cmap='gray')
plt.title(titles[0])

plt.subplot(1,3,2)
plt.imshow(output[1], cmap='gray')
plt.title(titles[1])

plt.subplot(1,3,3)
plt.imshow(output[2], cmap='gray')
plt.title(titles[2])
plt.show()
        

#windowname = 'rotated op' 
#cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
#cv2.imshow(windowname,o)

