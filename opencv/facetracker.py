import cv2
import numpy as np

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('D:\\VS CODE\\project-py\\opencv\\face_detect.xml')
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faceRect = faceCascade.detectMultiScale(gray, 1.5, 3)
    for (x, y, w, h) in faceRect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0),2)
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break