import cv2
import numpy as np

imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest4.jpg' # path for region of interest image
imgpath2 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest1.jpg' # path for target image

roi = cv2.imread(imgpath1,1)
hsvi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

target = cv2.imread(imgpath2,1)
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsvi],[0, 1], None, [180, 256], [0, 180, 0, 256] )


# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
disc1 = cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(disc1,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)
#res = np.vstack((target,thresh,res))

#img5 = cv2.erode(res, np.ones((3, 3), np.uint8), iterations=3 )

#img6, contours, hierarchy = cv2.findContours(res, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cnt = contours[0]

#(x,y),radius = cv2.minEnclosingCircle(cnt)
#center = (int(x),int(y))
#radius = int(radius)
#target = cv2.circle(target,center,radius,(0,255,0),2)

windowname = 'test'
cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
cv2.imshow('test',hsvt)

#closing the image window
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
