import cv2
import numpy as np

def empty(v):
    pass

# img = cv2.imread('D:\VS CODE\project-py\opencv\XiWinnie.jpg')
# img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracker')
cv2.resizeWindow('Tracker', 640, 320)

cv2.createTrackbar('Hue Min', 'Tracker', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'Tracker', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'Tracker', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'Tracker', 255, 255, empty)
cv2.createTrackbar('Val Min', 'Tracker', 0, 255, empty)
cv2.createTrackbar('Val Max', 'Tracker', 255, 255, empty)

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSV比較好過濾顏色

while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'Tracker')
    h_max = cv2.getTrackbarPos('Hue Max', 'Tracker')
    s_min = cv2.getTrackbarPos('Sat Min', 'Tracker')
    s_max = cv2.getTrackbarPos('Sat Max', 'Tracker')
    v_min = cv2.getTrackbarPos('Val Min', 'Tracker')
    v_max = cv2.getTrackbarPos('Val Max', 'Tracker')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask) #img and img 套 mask

    cv2.imshow('img', img)
    # cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    cv2.waitKey(1)