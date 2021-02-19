import numpy as np
import cv2

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #BGR channels
        blue=int(img[y,x,0])
        green=int(img[y,x,1])
        red=int(img[y,x,2])

        print(blue)
        print(green)
        print(red)

        strBgr = str(blue)+","+str(green)+","+str(red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,strBgr,(x,y),font,.5,(blue,green,red),2)
        return(cv2.imshow("image",img))
    
# img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("./static/Lenna.jpg")
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

