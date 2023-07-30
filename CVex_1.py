#import open cv modules
import cv2

# reading image stored in python directory
img = cv2.imread('1.jpg',0)

#for resizing the window to fit the screen
cv2.namedWindow('pic',cv2.WINDOW_NORMAL)  

#showing the image file
cv2.imshow('pic',img)

# waiting for the user to enter key
cv2.waitKey(0)

#close the opened image window
cv2.destroyAllWindows()
