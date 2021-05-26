
import cv2 
import numpy as np 
  
# to read the image. 
img = cv2.imread('/home/hardik/Kratos_LD_QSTP/img4.jpg', cv2.IMREAD_COLOR) 
output = img.copy()
  
# converting to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# blurring using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (3, 3)) 
  
# Applying Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40) 
  
# to draw circles that are detected. 
if detected_circles is not None: 
  
    # Converting the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # to draw the circumference of the circle. 
        cv2.circle(output, (a, b), r, (0, 255, 0), 2) 
  
        # to draw a rectangle to show the center. 
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        cv2.imshow("Detected Circle", output) 
        cv2.waitKey(0) 
