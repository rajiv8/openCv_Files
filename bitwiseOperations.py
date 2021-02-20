
import cv2
import numpy as np 

# for finding the co-ordinates and creatingand saving image1.jpg
"""
img = np.zeros((250,500,3),np.uint8)
img = cv2.rectangle(img,(0,0),(251,511),(255,255,255),-1)
def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,",",y)  # x, y are co-ordinates of clicks 
        cv2.imshow('Image',img)
# cv2.imshow("Image",img)
cv2.imwrite("./static/image1.jpg",img)
cv2.setMouseCallback('Image',click_event)
 """
img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread("./static/image1.jpg")

bitAnd = cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitNot = cv2.bitwise_not(img1)
bitXor = cv2.bitwise_xor(img1,img2)

cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("BitAnd",bitAnd)
cv2.imshow("bitOr",bitOr)
cv2.imshow("bitNot",bitNot)
cv2.imshow("bitXor",bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()









