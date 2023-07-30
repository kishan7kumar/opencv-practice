#***************SCALING OPERATION ON IMAGES***********

import cv2
import matplotlib.pyplot as  plt
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1279.jpg'
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
output = cv2.resize(img1, None, fx=4, fy=1.5, interpolation = cv2.INTER_AREA)
plt.imshow(output)
plt.title('output')
plt.show()
