
# PROGRAM TO MAKE BGR COLOR PALETTE 

import cv2
import numpy as np

def emptyfunction():
    pass

img1 = np.zeros((512,512,3), np.uint8)
windowName = 'Opencv BGR color palette'
cv2.namedWindow(windowName)

# to refresh the image continuosly


cv2.createTrackbar('B',windowName,0,255,emptyfunction)
cv2.createTrackbar('G',windowName,0,255,emptyfunction)
cv2.createTrackbar('R',windowName,0,255,emptyfunction)



while(True):
     cv2.imshow(windowName,img1)

     if cv2.waitKey(1) == 27:    # here 27 repreent "esc" key 
         break

     blue = cv2.getTrackbarPos('B',windowName)
     green = cv2.getTrackbarPos('G',windowName)
     red = cv2.getTrackbarPos('R',windowName)

     img1[:] = [blue,green,red]
     print(blue,green,red)


cv2.destroyAllWindows()
