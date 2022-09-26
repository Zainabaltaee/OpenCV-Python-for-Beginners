import cv2

img=cv2.imread("Resources/lena.jpg")
Mask=cv2.imread("Resources/horse_r.png")
Mask=cv2.resize(Mask,(img.shape[1],img.shape[0]))
img2=cv2.bitwise_and(img,Mask)
print(img.shape)
print(Mask.shape)

cv2.imshow("Image",img)
cv2.imshow("Mask",Mask)
cv2.imshow("masking",img2)

cv2.waitKey(0)