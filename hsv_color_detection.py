import cv2
import numpy as np

# for video capturing
cap = cv2.VideoCapture(0)

def nothing(x):
    print(x)

cv2.namedWindow("HSV_TrackBar")

cv2.createTrackbar("LowerHue","HSV_TrackBar",0,255,nothing)
cv2.createTrackbar("LowerSaturation","HSV_TrackBar",0,255,nothing)
cv2.createTrackbar("LowerValue","HSV_TrackBar",0,255,nothing)
cv2.createTrackbar("UpperHue","HSV_TrackBar",255,255,nothing)
cv2.createTrackbar("UpperSaturation","HSV_TrackBar",255,255,nothing)
cv2.createTrackbar("UpperValue","HSV_TrackBar",255,255,nothing)

while True:
    # for image 
    # frame = cv2.imread("./static/smarties2.png")
    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    """
    # to detect blue color lower bound and upper bound for blue 
    l_b = np.array([110,50,50])
    u_b = np.array([130,255,255])
    """
    l_h = cv2.getTrackbarPos("LowerHue","HSV_TrackBar")
    l_S = cv2.getTrackbarPos("LowerSaturation","HSV_TrackBar")
    l_V = cv2.getTrackbarPos("LowerValue","HSV_TrackBar")

    U_h = cv2.getTrackbarPos("UpperHue","HSV_TrackBar")
    U_S = cv2.getTrackbarPos("UpperSaturation","HSV_TrackBar")
    U_V = cv2.getTrackbarPos("UpperValue","HSV_TrackBar")
    
    # values from trackbars 
    l_b = np.array([l_h,l_S,l_V])
    u_b = np.array([U_h,U_S,U_V])

    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("RES",res)


    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()