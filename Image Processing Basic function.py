import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("Resources/Lena.png")
imgCanny=cv2.Canny(img,150,200)
imgdilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgerode=cv2.erode(imgdilation,kernel,iterations=1)
cv2.imshow("BGR IMAGE",img)
cv2.imshow("canny image",imgCanny)
cv2.imshow("dilate image",imgdilation)
cv2.imshow("erosion image",imgerode)


cv2.waitKey(0)