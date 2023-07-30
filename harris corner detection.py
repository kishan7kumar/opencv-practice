import cv2
import numpy as np
imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest Image\\1.jpg'
img = cv2.imread(imgpath1,1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04) #(image, blocksize=size of neigbourhood,ksize=aperature size of sobel,k= haris detetor free parameter)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.05*dst.max()]=[0,0,255]
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()