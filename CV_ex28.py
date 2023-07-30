# ROTATING IMAGES IN LOOP

#importing all modules
import cv2
import time

#importing image from folder
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1279.jpg'

#reading images in color and converting into rgb channel
img1 = cv2.imread(imgpath1,1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
rows, columns, channels = img1.shape
angle = 0

while True:
    if angle==360:  #for continous motion 
        angle = 0;
    R = cv2.getRotationMatrix2D((columns/2, rows/2),angle,0.5)  #changing angle to -angle will anticlocwise
    output = cv2.warpAffine(img1, R, (columns, rows))

    #creating a normal sized window
    windowname = 'rotated op' 
    cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
    cv2.imshow(windowname,output)

    #rotating by angle
    angle = angle + 1 
    time.sleep(0.01)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
    
    
