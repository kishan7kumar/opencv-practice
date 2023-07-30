#import open cv modules
import cv2

#importing matplotlib module
import matplotlib.pyplot as plt

# taking images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1280.jpg'

# reading image from the path set above
img = cv2.imread(imgpath,1)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting the color space
plt.imshow(img) # cmap = 'gray')
plt.title('BGR colormap')
plt.xticks([])   #for x axis 
plt.yticks([])  # for y axis
plt.show()

#plt.imshow(img, cmap = 'Spectral')
#plt.title('Spectral colormap')
#plt.xticks([])
#plt.yticks([])
#plt.show()
