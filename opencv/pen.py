import cv2
import numpy as np

cap = cv2.VideoCapture(0)

penColorHSV = [[83, 161, 110, 94, 234, 142],
               [151, 44, 128, 179, 184, 248],
               [18, 132, 160, 28, 231, 255]] #GREEN PINK ORANGE

penColorBGR = [[0 , 255, 0],
               [0, 0, 255],
               [255, 0, 0]]

DrawPoints = []

def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask = mask) #img and img 套 mask
        penx, peny = findContour(mask)
        cv2.circle(imgContour, (penx, peny), 10, penColorBGR[i], cv2.FILLED)
        if peny != 0:
            DrawPoints.append([penx, peny, i])
        # cv2.imshow('result',result)


def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
        area = cv2.contourArea(cnt)
        if area > 50:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)
            # cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)

    return x+w//2, y

def draw(drawpoints):
    for point in drawpoints:
        cv2.circle(imgContour, (point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)

while True:
    ret, frame = cap.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow('video', frame)
        findPen(frame)
        draw(DrawPoints)
        cv2.imshow('Contour', imgContour)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break