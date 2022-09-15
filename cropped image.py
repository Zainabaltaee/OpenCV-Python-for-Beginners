import cv2
img=cv2.imread("Resources/lambo.png")
print(img.shape)
imgcropped=img[0:200,200:500]
cv2.imshow("Image",img)
cv2.imshow("Image Cropped",imgcropped)

cv2.waitKey(0)