#import open cv modules
import cv2

# taking images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1280.jpg'
#imgpath = 'C:\\Users\\kishan\\Pictures\\Goa\\'
#imgpath1 = imgpath + 'flamenew.jpg'
# reading image from the path set above
img = cv2.imread(imgpath,0)
#for resizing the window to fit the screen
#showing the image file
cv2.imshow('pic', img)

# waiting for the user to enter key

# to close specific windows
   # cv2.destroyWindow('pic')
