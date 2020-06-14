import cv2
print("Package Imported!")

#image
# img = cv2.imread("image1.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#video
#cap=cv2.VideoCapture("Clock_Face_3Videvo.mov")

#webcam
cap=cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100) #brightness

while True:
    success,img=cap.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break