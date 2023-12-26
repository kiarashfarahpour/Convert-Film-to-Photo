import cv2

cap = cv2.VideoCapture("D:\Video.mp4")

i = 0

while i < 10:
    
    i = i + 1

    success, img = cap.read()

    if success:

        cv2.imwrite("Frames/%d.jpg" % i, img)


