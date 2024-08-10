#accessing my webcam using OpenCV and python
import cv2
from matplotlib import pyplot as plt

#connecting to webcam
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not vid.isOpened():
    print("Can't open camera")
    exit()

vid.set(3, 640)
vid.set(4, 480)

while True:
    ret, img = vid.read()
    if not ret:
        print("Can't receive frame")
        break
    
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()