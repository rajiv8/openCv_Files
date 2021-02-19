# basic Operations 

import cv2

img = cv2.imread("./static/messi.jpg")
img2 = cv2.imread("./static/Lenna.jpg")
print(img.shape) # returns rows,columns and channels 
print(img.size)  # total no.of pixels 
print(img.dtype) # returns datatype

# b,g,r = cv2.split(img) #splitting the three channels 

# resizing the image - first method 
scale_percent=40 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize=(width,height)
# output = cv2.resize(img, dsize)

# second method
img= cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

# b,g,r = cv2.split(output) #splitting the three channels after resizing
# print(output.shape) # checking the shape of resized image 
# img = cv2.merge((b,g,r)) # merging the three channels 

# `def click_event(event,x,y,flags,params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,",",y)  # x, y are co-ordinates of clicks 
#         cv2.imshow('image',output)

# output = cv2.rectangle(output,(544,562),(670,652),(0,0,255),5)
# output = cv2.rectangle(output,(502,520),(639,657),(0,0,255),5)

# ball = output[544:562,652:670]
# output[502:520,639:657] = ball

adding = cv2.add(img,img2) # for simply adding the image 
adding = cv2.addWeighted(img,0.4,img2,0.3,0) # for inhancing the images 
cv2.imshow("image",adding)
# cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()