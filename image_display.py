import cv2
from matplotlib import pyplot as plt

image = cv2.imread('input_img.jpg') 

# cv2.imshow('image display', image)
# cv2.waitKey(0)

plt.imshow(image)
plt.show()