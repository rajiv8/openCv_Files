import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./static/gradient.png",0)
# cv2.imshow("Image",img)

# since matplotlib reads RGB and cv2 reads BGR
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# threshold gives two outputs first is threshhold value and second is Image 
_,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
# print(_)
_,th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
_,th4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

titles = ["original_image","Binary","Binary_Inv","To_Zero","To_Zero_Inv","Trunc"]
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.xticks([])
    plt.yticks([])

plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()