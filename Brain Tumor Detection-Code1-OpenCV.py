import cv2
import numpy as np

#IMPORTING IMAGES
img = cv2.imread("Resources/y0.jpg")
cv2.imshow("Original Image", img)

#CONVERTING TO GRAY SCALE IMAGE
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, 0.7)
cv2.imshow("GRAYSCALE IMAGE",img1)
#THRESHOLDING THE IMAGE(THRESHOLD VALUE OF PIXEL IS -155)
img2: object
(T, img2) = cv2.threshold(img1, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholding",img2)
#INVERSE THRESHOLDING THE IMAGE(THRESHOLD VALUE OF PIXEL IS -155)
(T, img3) = cv2.threshold(img1, 155, 255,cv2.THRESH_BINARY_INV)
cv2.imshow("InerseThresholding",img3)
#(img3-INVERSE THRESHOLDING,img2-THRESHOLDING)

#MORPHOLOGICAL OPERATION(to remove unwanted part from thresholding image)
kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (10,5))
img4 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
cv2.imshow("MORPHOLOGIACAL OPERATION",img4)

#MORPHOLOGICAL OPERATION
img5 = cv2.erode(img4, None, iterations = 14)
img6 = cv2.dilate(img5, None, iterations = 13)
cv2.imshow("MORPHOLOGICAL OPERATION:",img6)


#CANNY EDGE DETECTOR
img7= cv2.Canny(image=img6, threshold1=100, threshold2=200)
cv2.imshow('Canny Edge Detection', img7)

#CONTOURS
(cnts,_)=cv2.findContours(img7.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, cnts,-1, (0,0,255),2)
cv2.imshow("CONTOURS",img)
cv2.waitKey(0)

