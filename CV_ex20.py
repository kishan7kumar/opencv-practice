#  ********* BLENDING AND TRANSITIONING IMAGES *********

#import open cv modules
import cv2
import time
import numpy as np

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

for i in np.linspace(0,1,10):
    alpha = i
    beta = 1 - alpha
    cv2.namedWindow('transition',cv2.WINDOW_NORMAL)
    output = cv2.addWeighted(imgnew1,alpha,imgnew2,beta,0)
    
    cv2.imshow('Transition',output)
    time.sleep(0.25)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
#alpha = 0.7
#beta = 0.3
#gamma = 0

#output = cv2.addWeighted(imgnew1, alpha, imgnew2, beta, gamma)


#titles = ['image 1', 'image 2', 'weighted addition']
#images = [imgnew1, imgnew2, output]

# for loops for more number of images
#for i in range(3):
 #   plt.subplot(1, 3, i+1)        # two row one column position starts from 1 
  #  plt.imshow(images[i])
   # plt.title(titles[i])
    #plt.xticks([])   #for x axis 
   # plt.yticks([])  # for y axis
#plt.show()
