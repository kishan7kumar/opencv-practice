import cv2
import numpy as np

imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest Image\\1.jpg'
img = cv2.imread(imgpath1,1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
#sift = cv2.SIFT()   #non free module
(kps, descs) = sift.detectAndCompute(gray, None)
#kp = sift.detect(gray,None)
img1=cv2.drawKeypoints(gray,kps,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#img1=cv2.drawKeypoints(gray,kp)
cv2.imshow('img1',img1)