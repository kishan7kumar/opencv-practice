#  ********* TRACKBAR IMAGE BLENDING *********

#import open cv modules
import cv2

def emptyfunction():
    pass
# taking images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
img1 = imgpath + 'IMG_1279.jpg'
img2 = imgpath + 'IMG_1290.jpg'

imgnew1 = cv2.imread(img1,1)
imgnew2 = cv2.imread(img2,1)

output = cv2.addWeighted(imgnew1,0.5,imgnew2,0.5,0)
windowname = "transition demo"   
cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
cv2.createTrackbar('Alpha',windowname,0,1000,emptyfunction)
    
while(True):
    cv2.imshow(windowname,output)    
    if cv2.waitKey(1)==27:
        break

    alpha = cv2.getTrackbarPos('Alpha',windowname)/1000
    beta = 1- alpha
  
    output = cv2.addWeighted(imgnew1,alpha,imgnew2,beta,0)
    print(alpha,beta)
   
cv2.destroyAllWindows()
