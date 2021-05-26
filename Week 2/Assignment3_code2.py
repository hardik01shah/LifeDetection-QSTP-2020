import cv2
import numpy as np

image = cv2.imread('/home/hardik/Kratos_LD_QSTP/img3.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Original",image)
cv2.imshow("Converted to RGB",image_rgb)
cv2.imshow("Converted to Grayscale",image_gray)
cv2.imshow("Converted to HSV",image_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#changes noted:
#1.BGR to RGB:
# Evidently, Red and blue colors in the image get interchanged and the backround colors appeared to have fade and image was mostly gray
#2.BGR to HSV
# Patches of color appeared in places and small minute pixels of different colors were distributed throughout the image
#3. BGR to Grayscale
#image became a complete a gray color