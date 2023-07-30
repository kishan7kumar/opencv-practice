#import open cv modules
import cv2

import numpy as np

# taking images from desired path
#imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\IMG_1280.jpg'

# making entire image black 
img1  = np.zeros((512,512,3),np.uint8)

# reading image from the path set above
#img = cv2.imread(imgpath)

#for resizing the window to fit the screen
cv2.namedWindow('pic',cv2.WINDOW_NORMAL)  

#for drawing line on image
#cv2.line(img1, (0,200), (400,0), (0,0,255), 2)

#for drawing rectangle
#cv2. rectangle(img1,(80,100), (300,23), (0,255,0), 4)

# for drawing circle with center and radius 
#cv2.circle(img1,(200,200),70,(0,0,255),4)  #replace thickness with -1 to fill the color into circle


#for drawing ellipse centre,major and minor axes,roation,portiondegrees,thickness
#cv2.ellipse(img1,(50,50),(50,20),20,0,360,(127,127,127), -1)


#to draw a polygon with specified points
points = np.array([[80,2],[125,0],[179,0],[230,5],[30,50]],np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(img1, [points],True,(0,255,255))


#to display custom text image black image
text1 = 'this is text'
cv2.putText(img1,text1,(50,300),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0))

#showing the image file
cv2.imshow('pic',img1)





# waiting for the user to enter key
#cv2.waitKey(0)

#close the all opened image window
#cv2.destroyAllWindows()               

# to close specific windows
   # cv2.destroyWindow('pic')
