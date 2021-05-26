import cv2
 
img = cv2.imread('/home/hardik/Kratos_LD_QSTP/img3.jpg')
cv2.imshow("Original",img)
 
img_inv = cv2.bitwise_not(img)
cv2.imshow("Inverted",img_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Changes Noted:
#colors are interchanged, black is diplayed as white, red as blue and so on....