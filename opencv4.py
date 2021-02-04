# writing the video 

# importing cv2 library
import cv2 

# capturing the live camera
cap = cv2.VideoCapture(0)

# defining fourcc(its a 4 char code)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

# defining the output file
out = cv2.VideoWriter('./static/output.avi',fourcc,20.0,(640,480))

# looping the video if its true - isOpened returns boolean 
while(cap.isOpened()):
    # reading the video
    ret,frame = cap.read()

    if ret == True:
        
        # writing the video 
        out.write(frame)

        # converting the video to gray
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # showing the frame
        cv2.imshow('Frame',gray)
        
        # if q is pressed video terminates 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# releasing the frames   
cap.release()
out.release()

# destroying the windows
cv2.destroyAllWindows()
