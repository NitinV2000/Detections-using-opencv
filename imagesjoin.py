import cv2
import numpy as np

img = cv2.imread("lena.jpg")
hor = np.hstack((img,img)) # Must have same channels
#Take stackImages code from online where it will stack all images properly without the problem of channels
# Using
# imgStack = stackImages(0.5,([img,img,img],[img,img,img]))
cv2.imshow("Horizontal",hor)


cv2.waitKey(0)