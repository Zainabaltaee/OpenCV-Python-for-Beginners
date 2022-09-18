import numpy as np
import cv2
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), (255,255,255), -1)
cv2.imshow("Rectangle", rectangle)
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, (255,255,255),-1)
#cv2.imshow("Circle", circle)
bit_and=cv2.bitwise_and(rectangle,circle)

bit_or=cv2.bitwise_or(rectangle,circle)
cv2.imshow("result",bit_or)

bit_xor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow("result",bit_xor)

bit_not=cv2.bitwise_not(rectangle)
cv2.imshow("result",bit_not)

cv2.waitKey(0)