import numpy as np
import cv2
from matplotlib import pyplot as plt

imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest Image\\1.jpg'
bgr_image = cv2.imread(imgpath1,1)
rgb_image = cv2.cvtColor(bgr_image,cv2.COLOR_BGR2RGB)
rgb = rgb_image
#creating mask and models
mask = np.zeros(rgb_image.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#defining our subject
rect = (50,50,600,400)
cv2.grabCut(rgb_image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
rgb_image = rgb_image*mask2[:,:,np.newaxis]

plt.subplot(1,2,1)
plt.imshow(rgb)
plt.title('Original Image')
plt.subplot(1,2,2)

plt.imshow(rgb_image)
plt.title('Grab cut image')
plt.colorbar()
plt.show()