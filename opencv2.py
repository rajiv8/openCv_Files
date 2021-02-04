# Reading the video 

# importing cv2 library
import cv2 

# captures the live camera 
cap = cv2.VideoCapture(0)   # cv2.VideoCapture(0) - if wants to capture video file

# for looping the video 
while(True):
    ret,frame = cap.read() 
    # .read() gives two values one is boolean which stores in ret,
    # second is if the boolean values is true then it captures the frame which is tored in ferame variable

    # now Show the captured Frame 
    cv2.imshow("Frame",frame)

    # cv2.waitkey(1) - for video wait 
    if cv2.waitKey(1) & 0xFF== ord('q'): # if q is pressed video terminates 
        break

# now release the frames 
cap.release()

# destroy all the windows
cv2.destroyAllWindows()


