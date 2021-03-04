import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./static/smarties.png",cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

# merphological Transformation

kernal = np.ones((4,4),np.uint8)

dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=1)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
morph_gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
top_hat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)


titles = ["image","mask","dilation","erosion","opening","closing","morph_gradient","top_hat"]
images = [img,mask,dilation,erosion,opening,closing,morph_gradient,top_hat]

for i in range(len(images)):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()