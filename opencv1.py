import cv2
"""
# reading the image 
img = cv2.imread("./static/Lenna.jpg",flags=0) # flags:0-grayscale, 1-colored,-1-inluding alpha channel

# prints the matrix of img
print(img)

# shows the img
cv2.imshow("Image",img)

# stops the image until any key is pressed
cv2.waitKey(0)

# destroy all the windows if key is pressed
cv2.destroyAllWindows()

# for copying the image 
cv2.imwrite("./static/lenna2.jpg",img)  """

# well structured program 

img = cv2.imread("./static/Lenna.jpg",1)
cv2.imshow(".Lenna Image",img)
k = cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("./static/Lenna3.jpg",img)
    cv2.destroyAllWindows()





