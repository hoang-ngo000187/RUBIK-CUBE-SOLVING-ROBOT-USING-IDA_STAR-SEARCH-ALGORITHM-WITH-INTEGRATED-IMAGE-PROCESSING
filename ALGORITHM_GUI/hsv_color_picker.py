import cv2
import numpy as np

def Min_H(pos):
    Min_H.value = pos
Min_H.value = 0

def Min_S(pos):
    Min_S.value = pos
Min_S.value = 0

def Min_V(pos):
    Min_V.value = pos
Min_V.value = 0

def Max_H(pos):
    Max_H.value = pos
Max_H.value = 255

def Max_S(pos):
    Max_S.value = pos
Max_S.value = 255

def Max_V(pos):
    Max_V.value = pos
Max_V.value = 255

cv2.namedWindow("Control")
cv2.resizeWindow("Control",(300,300))
cv2.createTrackbar("Min H", "Control", 0, 180, Min_H)
cv2.createTrackbar("Min S", "Control", 0, 255, Min_S)
cv2.createTrackbar("Min V", "Control", 0, 255, Min_V)

cv2.createTrackbar("Max H", "Control", 180, 180, Max_H)
cv2.createTrackbar("Max S", "Control", 255, 255, Max_S)
cv2.createTrackbar("Max V", "Control", 255, 255, Max_V)

#im = cv2.imread('rubik5.jpg')
#im = cv2.bilateralFilter(im,9,75,75)
#hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   # HSV image

url = "http://192.168.0.3:4747/video"
id = 0
cap = cv2.VideoCapture(0)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

while True:
    _, img = cap.read()
    height, width, _ = img.shape

    square_size_factor=0.4
    square_x1=int((width-((square_size_factor)*height))/2)
    square_x2=int((width+((square_size_factor)*height))/2)


    square_y1=int(((1-square_size_factor)/2)*height)
    square_y2=int(((1+square_size_factor)/2)*height)

    cv2.rectangle(img, (square_x1, square_y1), (square_x2, square_y2), (255,0,0), 2)
    #cv2.imshow("Frame", img)
    
    img = cv2.bilateralFilter(img,9,75,75)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # HSV image
    lower = np.array([Min_H.value, Min_S.value, Min_V.value])
    upper = np.array([Max_H.value, Max_S.value, Max_V.value])
    mask_sub = cv2.inRange(hsv_img , lower, upper) # lọc ra những pixel có giá trị nằm trong vùng đã chọn

    mask = cv2.merge((mask_sub,mask_sub,mask_sub))

    res = cv2.bitwise_and(img,mask)

    #cv2.imshow("Mask_sub", mask_sub)
    imgStack = stackImages(0.8, ([img, mask, res]))
                                 #[imgDil, imgContour, imgContour]))
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Result", res)
    cv2.imshow("Result", imgStack)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.waitKey()
cap.release()
cv2.destroyAllWindows()
