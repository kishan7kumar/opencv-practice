#  ******* ARITHMETIC OPERATION ON IMAGES*********

#import open cv modules
import cv2

#importing matplotlib module
import matplotlib.pyplot as plt

# taking images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
img1 = imgpath + 'IMG_1279.jpg'
img2 = imgpath + 'IMG_1290.jpg'

imgnew1 = cv2.imread(img1,1)
imgnew2 = cv2.imread(img2,1)

imgnew1 = cv2.cvtColor(imgnew1,cv2.COLOR_BGR2RGB)
imgnew2 = cv2.cvtColor(imgnew2,cv2.COLOR_BGR2RGB)
imgnew3 =  imgnew1 + imgnew2 #   imgnew1 / imgnew2   imgnew1 * imgnew2   # imgnew3 = imgnew1 + 50
imgnew4 = imgnew1 - imgnew2
imgnew5 = imgnew2 - imgnew1

titles = ['image 1', 'image 2', 'image 3', 'image 1 - image 2', 'image 2 - image 1']
images = [imgnew1, imgnew2, imgnew3, imgnew4, imgnew5]

# for loops for more number of images
for i in range(5):
    plt.subplot(1, 5, i+1)        # two row one column position starts from 1 
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])   #for x axis 
    plt.yticks([])  # for y axis
plt.show()
