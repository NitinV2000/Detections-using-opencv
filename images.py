import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
# cap = cv2.VideoCapture("tree.avi")

# while True:     # put (cap.isOpened())
#     success, frame = cap.read()
      #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Video",frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): write it in this way
#         break
# cv2.imwrite creates a file.


img = cv2.imread("lena.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=2) #To thicker the edges
imgEroded = cv2.erode(imgDialation,kernel,iterations=2) # Opposite of Dilation
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image", imgCanny) # edge detector
cv2.imshow("Dialated Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

# opencv has opposite y and x axis

