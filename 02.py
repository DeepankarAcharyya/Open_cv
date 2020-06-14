import cv2
import numpy as np

img = cv2.imread("image1.jpg")

#gray scale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", imgGray)

#blur image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #kernel size-> odd number
#cv2.imshow("Blur Image", imgBlur)

#edge detector
imgCanny = cv2.Canny(img, 100, 100)
#cv2.imshow("Canny Image", imgCanny)

#image dilation
imgDilation = cv2.dilate(imgCanny,np.ones((5,5)), iterations=2)
cv2.imshow("Dialation Image", imgDilation)

#image errosion
imgEroded = cv2.erode(imgDilation, np.ones((5, 5)), iterations=2)
cv2.imshow("Erosion Image", imgEroded)

cv2.waitKey(0)
