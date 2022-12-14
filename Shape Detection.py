
import cv2

img = cv2.imread('Resources/1.png')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.THRESH_BINARY_INV)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
    x,y = approx[0][0]

    if len(approx) == 3:
        cv2.putText( img, "Tri", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0),2 )
    elif len(approx) == 4 :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0),2)

        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0),2)

    elif len(approx) == 5 :
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0),2)
    elif len(approx) == 10 :
        cv2.putText(img, "star", (x-10, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0),2)
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0),2)

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
