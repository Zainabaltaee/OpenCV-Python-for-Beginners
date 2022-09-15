import cv2
img=cv2.imread("Resources/lambo.png")
print(img.shape)
height=1200
width=800
imgnew=cv2.resize(img,(width,height))
print(imgnew.shape)

cv2.imshow("Image",img)
cv2.imshow(" Resize Image",imgnew)

cv2.waitKey(0)