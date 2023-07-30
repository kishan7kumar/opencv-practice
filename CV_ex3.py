#import open cv modules
import cv2

# taking images from desired path
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1280.jpg'

# reading image from the path set above
img = cv2.imread(imgpath,1)      #1  color image reading {defaultmode}
#img = cv2.imread(imgpath,0)     #0  graysacle image reading
#img = cv2.imread(imgpath,-1)    #-1 maintains alpha transparency channel

# selecting the image writing path
imgout = 'C:\\Users\\kishan\\Pictures\\rpiimages\\IMG_1280.tiff'

#for resizing the window to fit the screen
cv2.namedWindow('pic',cv2.WINDOW_NORMAL)  

#showing the image file
cv2.imshow('pic',img)

#for writing the image to the path
cv2.imwrite(imgout,img)

# waiting for the user to enter key
cv2.waitKey(0)

#close the all opened image window
cv2.destroyAllWindows()               

# to close specific windows
   # cv2.destroyWindow('pic')

