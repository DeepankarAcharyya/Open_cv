import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #brightness

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, 80, 50)
    cv2.imshow("video", imgCanny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
