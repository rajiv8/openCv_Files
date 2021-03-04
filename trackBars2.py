import cv2

def nothing(x):
    print(x)

cv2.namedWindow("image")

cv2.createTrackbar("CP","image",0,400,nothing)

switch= "Color / Grey"
cv2.createTrackbar(switch,"image",0,1,nothing)

while(1):
    img = cv2.imread("./static/Lenna.jpg")
    pos = cv2.getTrackbarPos("CP","image")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,5,(0,0,255),2)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
    s = cv2.getTrackbarPos(switch,"image")
    if s==0:
        pass
    else:
        # cnverting color image to gray if trackbar position is 1 
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("image",img)

cv2.destroyAllWindows()