import cv2

img = cv2.imread('D:\\VS CODE\\project-py\\opencv\\qq.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faceCascade = cv2.CascadeClassifier('D:\\VS CODE\\project-py\\opencv\\face_detect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 4) #img 縮小比例 最少被框幾次

print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0),2)

cv2.imshow('img', img)
cv2.waitKey(0)