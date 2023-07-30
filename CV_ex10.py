#import open cv modules
import cv2

#importing matplotlib module
import matplotlib.pyplot as plt

# taking images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1339.jpg'

# reading image from the path set above
img = cv2.imread(imgpath,0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


plt.imshow(img, cmap = 'gray')
plt.title('gray colormap')
plt.xticks([])   #for x axis 
plt.yticks([])  # for y axis
plt.show()

plt.imshow(img, cmap = 'Spectral')
plt.title('Spectral colormap')
plt.xticks([])
plt.yticks([])
plt.show()

#for resizing the window to fit the screen
#cv2.namedWindow('pic',cv2.WINDOW_NORMAL)  

#showing the image file
#cv2.imshow('pic',img)

# waiting for the user to enter key
#cv2.waitKey(0)

#close the all opened image window
#cv2.destroyAllWindows()               
