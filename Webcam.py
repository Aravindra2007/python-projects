import cv2

camera = cv2.VideoCapture(0)

success,image = camera.read()

if success:
    cv2.imwrite("ak.jpg",image)