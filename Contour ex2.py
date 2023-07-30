
import cv2
import numpy as np

#importing fire test image
imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest2.jpg'
img = cv2.imread(imgpath1, 0)
originalread = cv2.imread(imgpath1, 1)

#thresholding the image
ret, thresh = cv2.threshold(img, 200, 255, 0)

#eroding to remove noise
img2 = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=10 )

#finding contours
img1, contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#calculating number of contours and their location
cnt = contours[3]


#calculating moments
M = cv2.moments(cnt)
print (M)
#calculating area
area = cv2.contourArea(cnt)
print("area of contour = ", area)
#calculating perimeter
perimeter = cv2.arcLength(cnt, True)
print('perimeter of contour = ', perimeter)


#bounding rectangle on detected contour region
#x,y,w,h = cv2.boundingRect(cnt)   #cnt specifies the contour to be selected
#img = cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

#bounding the circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

#contour matching
cnt2 = contours[3]
cnt3 = contours[3]
ret = cv2.matchShapes(cnt2,cnt3,1,0.0)
print ('matching value of two contours = ',ret)

#displaying the output image with rectangle box
windowname = 'test'
cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
cv2.imshow('test',img)

#closing the image window
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
