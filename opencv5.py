# draw different shapes 

import numpy as np
import cv2

# img = cv2.imread('./static/Lenna.jpg',1)
img = np.zeros([512,512,3],np.uint8)

# for drawing line 
# cv2.line(img,start co-ord,end co-ord,color,thickness)
img = cv2.line(img,(0,255),(255,255),(0,0,255),3)

# for arrowed line
img = cv2.arrowedLine(img,(0,0),(255,255),(0,255,0),3)

# for rectangle 
# cv2.rectangle(img,top_left_co-ord,low_right_co-ord,color,thickness)
# if thickness -1 then,rectangle filled with color
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)

# for circle
# cv2.circle(img,center,radius,color,thickness)
img = cv2.circle(img,(447,63),20,(0,255,0),-1)

# For text
font = cv2.FONT_HERSHEY_SIMPLEX   #first declare the font
# cv2.putText(img,"TEXT",(origin_co-ord),decalared_font,size,color,thickness,linetype)
img = cv2.putText(img,"openCv",(10,500),font,4,(255,0,0),5,cv2.LINE_AA)


cv2.imshow("File",img)
cv2.waitKey(0)
cv2.destroyAllWindows()