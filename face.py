import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("lena.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# We use cascades to find objects, we can use other cascades also 
# or create custom cascades for other objects

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result", img)
cv2.waitKey(0)