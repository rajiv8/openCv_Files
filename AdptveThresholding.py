import cv2 

img = cv2.imread("./static/sudoku.png",0)

# simple thresholding
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# adaptive Thresholding
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,1)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,1)

cv2.imshow("Image",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()