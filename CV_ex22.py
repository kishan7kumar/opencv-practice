#  ********* SPLIITING AND MERGING CHANNELS OF COLOR IMAGE *********

#import open cv modules
import cv2

import matplotlib.pyplot as plt

#images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1279.jpg'


img = cv2.imread(imgpath1, 1)
imgnew = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(imgnew)

titles = ['Original image','red','green','blue']
images = [cv2.merge((r,g,b)), r, g, b]

plt.subplot(2, 2, 1)
plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([])
plt.yticks([])


plt.subplot(2, 2, 2)
plt.imshow(images[1],cmap ='gray')
plt.title(titles[1])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(images[2], cmap ='gray')
plt.title(titles[2])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(images[3], cmap = 'gray')
plt.title(titles[3])
plt.xticks([])
plt.yticks([])

plt.show()