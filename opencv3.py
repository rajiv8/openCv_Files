# showing the video as grayscale

# importing cv2 library
import cv2

# captures the live camera 
cap = cv2.VideoCapture(0)

# to get frame width
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# to get franme height 
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# looping the video 
while(True):
    ret,frame = cap.read()
    # .read() gives two values one is boolean which stores in ret,
    # second is if the boolean values is true then it captures the frame which is tored in ferame variable
    
    # converting the captured frame to gray scaled
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # show the frame 
    cv2.imshow("Frame",gray)

    # if q is pressed video terminates
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release all frames 
cap.release()

# destroy all windows
cv2.destroyAllWindows()
