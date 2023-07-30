#************ IMAGE THRESHOLDING IN OPENCV ***************


#importing all modules
import cv2
import matplotlib.pyplot as plt

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1339.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,0)
#img11 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)


th = 100
max_val = 130

ret, o = cv2.threshold(img1, th, max_val, cv2.THRESH_BINARY_INV)
#THRESH_BINARY_INV
#THRESH_TOZERO
#THRESH_TOZERO_INV
#THRESH_TRUNC


output = [img1, o]
titles = ['Original image', 'Sun detected']

#creating a normal sized window
plt.subplot(1,2,1)
plt.imshow(output[0], cmap='gray')
plt.title(titles[0])


plt.subplot(1,2,2)
plt.imshow(output[1], cmap='gray')
plt.title(titles[1])
plt.show()
        

#windowname = 'rotated op' 
#cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
#cv2.imshow(windowname,o)

    
    
