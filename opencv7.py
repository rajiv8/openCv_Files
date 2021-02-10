# Mouse events in opencv
# Mouse clicked co-ord

import cv2
import numpy as np

# to show all events in opencv
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# call back function
def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,",",y)  # x, y are co-ordinates of clicks 
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x)+","+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,255,0),2) 
        cv2.imshow('image',img)

img = np.zeros((512,512,3),np.uint8)  # black image 
cv2.imshow('image',img)

#calling the call back function
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()