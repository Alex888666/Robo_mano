
import cv2 as cv
import numpy as np


image = cv.imread("/home/papu/Desktop/Tec/7TO SEMESTRE/Manitas/Imgs/cuchillosbr.jpg")

#Escalación 
scale_percent = 20 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv.resize(image, dim, interpolation = cv.INTER_AREA)
ogimg = image.copy()

#Knife Detector
#CLAHE CON CLOR DETECTION
cv.cvtColor(image, cv.COLOR_BGR2HSV)
maskw = cv.inRange(image, (0, 0, 180), (255, 60, 255))
clahe =  cv.createCLAHE(clipLimit=40.0, tileGridSize=(5,5))
cl = clahe.apply(maskw)
cl = cv.bitwise_not(cl)
dilatew = cv.dilate(cl, (6, 6), iterations = 6)
erodew = cv.erode(dilatew, (6, 6), iterations = 6)
inv = (erodew-255)
ret, thresh = cv.threshold(inv, 127, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image, contours, -1, (0,0,255), 4)

#--------------------------------------------------------------------------------
#HAND DETECTION
sat = cv.cvtColor(ogimg, cv.COLOR_RGB2HSV)[:,:,1]
blur = cv.GaussianBlur(sat, (5,5),0)
ret, thresh2 = cv.threshold(blur, 100, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image, contours, -1, (255,0,0), 4)

cv.imshow("Result",image)
cv.imshow("Erodew",inv)
#cv.imshow("blur",cl)
#cv.imshow("cl1",cl) 
cv.waitKey(0)
cv.destroyAllWindows