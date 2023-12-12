import cv2
import numpy as np
import random
img = cv2.imread('D:\\VS CODE\\project-py\\opencv\\colorcolor.jpg')
# print(type(img))
# print(img.shape) 
# #R G B
# #B G R

# img = np.empty((300, 300, 3), np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] #B G R
newImg = img[0:150, 200:400]

cv2.imshow('img', newImg)
cv2.imshow('newImg', img)
cv2.waitKey(0)