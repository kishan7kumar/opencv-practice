# ********* DISPLAYING MULTIPLE IMAGES WITH MATPLOTLIB **********

#import open cv modules
import cv2

#importing matplotlib module
import matplotlib.pyplot as plt

# taking images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
img1 = imgpath + 'IMG_1279.jpg'
img2 = imgpath + 'IMG_1281.jpg'

imgnew1 = cv2.imread(img1,1)
imgnew2 = cv2.imread(img2,1)

imgnew1 = cv2.cvtColor(imgnew1,cv2.COLOR_BGR2RGB)
imgnew2 = cv2.cvtColor(imgnew2,cv2.COLOR_BGR2RGB)

titles = ['image 1', 'image 2']
images = [imgnew1, imgnew2]

# for loops for mroe number of images
for i in range(2):
    plt.subplot(1, 2, i+1)        # two row one column position starts from 1 
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])   #for x axis 
    plt.yticks([])  # for y axis
plt.show()
#plt.subplot(2,1,2)
#plt.imshow(imgnew2)
#plt.title('Spectral colormap')
#plt.xticks([])
#plt.yticks([])
#plt.show()
