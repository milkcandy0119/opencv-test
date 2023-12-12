import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 255 ,0), 2)
cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (300, 400), 30, (255, 0, 0), cv2.FILLED)
cv2.putText(img, "Hello", (100, 500), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 25, 0), 2) #no chinese


cv2.imshow('img', img)
cv2.waitKey(0)