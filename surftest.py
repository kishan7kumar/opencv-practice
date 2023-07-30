import cv2
import numpy as np
from matplotlib import pyplot as plt
imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest Image\\1.jpg'
img = cv2.imread(imgpath1,1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#sift = cv2.xfeatures2d.SIFT_create()
#(kps, descs) = sift.detectAndCompute(gray, None)
#print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
# kps: 274, descriptors: (274, 128)

surf = cv2.xfeatures2d.SURF_create(3000)
(kps, descs) = surf.detectAndCompute(gray, None)
print (len(kps))
#print(surf.hessianThreshold)
#print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
img2 = cv2.drawKeypoints(img,kps,None,(255,0,0),4)

plt.imshow(img2, cmap='gray')
plt.show()

#kps: 393, descriptors: (393, 64)B