import cv2

# cap = cv2.VideoCapture('D:\\VS CODE\\project-py\\opencv\\thump.mp4')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (1280,720))       
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break