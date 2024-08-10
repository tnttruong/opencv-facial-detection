import cv2
from matplotlib import pyplot as plt

imgPath = "\input_images\input_img.jpg"


#reads the img
img = cv2.imread(imgPath)
#print(img.shape)
#should print (4000, 2667, 3)
            #   B     G    R
# OpenCV uses Blue, Green, Red

#need to convert to grayscale for better efficiency
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(gray_img.shape) #no longer has 3rd color channel

#load Haar Cascade classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#perform face detection
face = face_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
#   scaleFactor = scale down size of input img to make it easier, reduces img size by 10%
#   minNeighbors = applies sliding window through img to detect faces

#drawing a bounding box around faces
for(x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0) , 4)
    
#display img in color
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#use Matplotlib to display img
plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('off')

plt.show()