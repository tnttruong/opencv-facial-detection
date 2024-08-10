import cv2

#load Haar Cascade classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not vid.isOpened():
    print("Can't open camera")
    exit()

#set resolution for webcam
vid.set(3, 640)
vid.set(4, 480)

#make green box around faces
def detect_bounding_box(vid):
    gray_img = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)

    #perform face detection
    face = face_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    for(x, y, w, h) in face:
        cv2.rectangle(vid, (x, y), (x+w, y+h), (0, 255, 0) , 4)

#loop for video
while True:
    ret, frame = vid.read()
    if not ret:
        print("Can't receive frame")
        break
    
    #apply function per frame
    face = detect_bounding_box(frame)
    
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()