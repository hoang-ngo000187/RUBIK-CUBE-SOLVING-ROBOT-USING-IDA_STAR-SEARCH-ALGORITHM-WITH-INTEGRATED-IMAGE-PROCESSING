import cv2
import numpy as np
from module import min,max,colorChar
def detect_color(img_clone):
    
    img_clone = cv2.bilateralFilter(img_clone,9,75,75)
    cv2.imshow("after apply filter", img_clone)
    hsv_img = cv2.cvtColor(img_clone, cv2.COLOR_BGR2HSV)
    mask=[]
    for i in range(6):
        m=cv2.inRange(hsv_img, min[i], max[i]) 
        mask.append(m)
        # cv2.imshow(colorChar[i], cv2.resize(m,(250,250)))
    contours=[]
    for i in range(6):
        _,m, _ = cv2.findContours(mask[i],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours.append(m)
    idx=0
    a = np.zeros((9, 3),dtype = 'int') 
    for i in range(6):
        for cnt in contours[i]:
            if cv2.contourArea(cnt)>50:
                x,y,w,h = cv2.boundingRect(cnt)
                a[idx]=(x,y,i)
                idx+=1
                cv2.putText(img_clone,colorChar[i],(x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),1,cv2.LINE_AA)
                cv2.rectangle(img_clone,(x,y),(x+w,y+h),(0,255,0),2)
    a = sorted(a, key= lambda y_Index: y_Index[1] , reverse = False)
    for i in range(0,3):
        a[i*3:i*3+3] = sorted(a[i*3:i*3+3], key= lambda x_Index: x_Index[0] , reverse = False)
    # print("after sort",a)
    result=np.zeros(( 9),dtype = 'str')
    mystring=""
    for i in range(0,9):
         mystring+=colorChar[a[i][2]]+"\t"   
    print("result :\t ", mystring)
    cv2.imshow("Result", img_clone)

img=cv2.imread('rub.jpg')
detect_color(img)

url = "http://192.168.0.4:4747/video"
id = 0
cap = cv2.VideoCapture(url)

while True:
    _, frame = cap.read()
    k = cv2.waitKey(1) & 0xff
    if k==27:#ESC is pressed
        break
    elif k==32:#SPACE is pressed
        detect_color(frame)
cap.release()
cv2.destroyAllWindows()
