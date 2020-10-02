import cv2
import numpy as np

# img = cv2.imread("lena.jpg")
# print(img.shape)
# imgResize = cv2.resize(img,(300,200))
# cv2.imshow("Image", img)
# cv2.imshow("Image Resize", imgResize)
# cv2.waitKey(0)

# img = cv2.imread("lena.jpg")
# imgCropped = img[0:200,200:400]
# cv2.imshow("Image", img)
# cv2.imshow("Image Cropped", imgCropped)

img = np.zeros((512,512,3),np.uint8) #uint8 gives numbers from 0 to 255
# print(img)
# img[:]=255,0,0   # whole image blue
cv2.line(img,(0,0),(200,200),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,250),(0,0,255),2) #cv2.FILLED to fill the rectangle
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),1)

cv2.imshow("Image",img)

cv2.waitKey(0)