import cv2
import time
from __init1__ import solve


url = "http://192.168.0.4:4747/video"

cap = cv2.VideoCapture(url)
# red_hsv=[[132,96,173],[157,136,225]]
# orange_hsv=[[0,80,203],[14,160,255]]
# white_hsv=[[94,27,200],[123,103,255]]
# #white_hsv=[[0,0,136],[49,34,212]]
# yellow_hsv=[[28,52,171],[34,198,255]]
# blue_hsv=[[89,160,171],[112,241,255]]
# # green_hsv=[[60,200,0],[85,255,255]] #cam thuong
# green_hsv=[[42,116,148],[52,226,255]]

# red_hsv=[[0,150,0],[5,255,120]]
# orange_hsv=[[5,150,121],[18,215,200]]
# white_hsv=[[100,0,0],[130,199,255]]
# #white_hsv=[[0,0,136],[49,34,212]]
# yellow_hsv=[[18,100,0],[35,255,255]]
# blue_hsv=[[100,200,70],[130,255,255]]
# # green_hsv=[[60,200,0],[85,255,255]] #cam thuong
# green_hsv=[[38,93,87],[65,255,249]]

red_hsv=[[152,185,53],[180,239,119]]
orange_hsv=[[170,177,160],[180,237,223]]
white_hsv=[[102,29,123],[115,59,200]]
yellow_hsv=[[35,169,150],[48,255,196]]
blue_hsv=[[112,182,55],[118,246,148]]
green_hsv=[[59,189,80],[70,255,152]]

#or 150<=h<=179
def find_color(h,s,v):#finds color given h,s,v values(average)
    if (red_hsv[0][0]<=h<=red_hsv[1][0] and red_hsv[0][1]<=s<=red_hsv[1][1] and red_hsv[0][2]<=v<=red_hsv[1][2]):
        return "F"
    elif (orange_hsv[0][0]<=h<=orange_hsv[1][0] and orange_hsv[0][1] <= s <= orange_hsv[1][1] and orange_hsv[0][2]<=v<=orange_hsv[1][2]):
        return "B"
    elif (yellow_hsv[0][0]<=h<=yellow_hsv[1][0] and yellow_hsv[0][1]<=s<=yellow_hsv[1][1] and yellow_hsv[0][2]<=v<=yellow_hsv[1][2]):
        return "D"
    elif (green_hsv[0][0]<=h<=green_hsv[1][0] and green_hsv[0][1]<=s<=green_hsv[1][1] and green_hsv[0][2]<=v<=green_hsv[1][2]):
        return "L"
    elif (white_hsv[0][0]<=h<=white_hsv[1][0] and white_hsv[0][1]<=s<=white_hsv[1][1] and white_hsv[0][2]<=v<=white_hsv[1][2]):
        return "U"
    elif (blue_hsv[0][0]<=h<=blue_hsv[1][0] and blue_hsv[0][1]<=s<=blue_hsv[1][1] and blue_hsv[0][2]<=v<=blue_hsv[1][2]):
        return "R"
    else:
        return 'U'
    # else:
    #     print("h ",h," s ",s," v ",v,"colour not recognised")

def color_detection_function(x, y, hsv, frame):
    pixel = hsv[x, y]

    hue = pixel[0]  # Lay gia tri Hue
    saturation = pixel[1]
    value = pixel[2]

    color = find_color(hue, saturation, value)
    return color

def one_side_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    height, width, _ = image.shape

    # pixel_1       pixel_2     pixel_3
    # pixel_4       pixel_5     pixel_6
    # pixel_7       pixel_8     pixel_9

    # Pick pixel_5
    x_5 = int(width / 2)
    y_5 = int(height / 2)
    color_5 = color_detection_function(x_5, y_5, hsv, frame)

    # Pick pixel_4
    x_4 = x_5
    y_4 = y_5 - 64
    color_4 = color_detection_function(x_4, y_4, hsv, frame)

    # Pick pixel_6
    x_6 = x_5
    y_6 = y_5 + 64
    color_6 = color_detection_function(x_6, y_6, hsv, frame)

    # Pick pixel_2
    x_2 = x_5 - 64
    y_2 = y_5
    color_2 = color_detection_function(x_2, y_2, hsv, frame)

    # Pick pixel_1
    x_1 = x_2
    y_1 = y_2 - 64
    color_1 = color_detection_function(x_1, y_1, hsv, frame)

    # Pick pixel_3
    x_3 = x_2
    y_3 = y_2 + 64
    color_3 = color_detection_function(x_3, y_3, hsv, frame)

    # Pick pixel_8
    x_8 = x_5 + 64
    y_8 = y_5
    color_8 = color_detection_function(x_8, y_8, hsv, frame)

    # Pick pixel_7
    x_7 = x_8
    y_7 = y_8 - 64
    color_7 = color_detection_function(x_7, y_7, hsv, frame)

    # Pick pixel_9
    x_9 = x_8
    y_9 = y_8 + 64
    color_9 = color_detection_function(x_9, y_9, hsv, frame)

    color = [color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8, color_9]
    color_side = "".join(str(x) for x in color)
    return color_side

i = 0
color = ""
while True:
    _, frame = cap.read()
    height, width, _ = frame.shape

    square_size_factor=0.4#fraction of height of image that square occupies
    square_x1=int((width-((square_size_factor)*height))/2)#coordinate calculation for square corners
    square_x2=int((width+((square_size_factor)*height))/2)


    square_y1=int(((1-square_size_factor)/2)*height)
    square_y2=int(((1+square_size_factor)/2)*height)

    cv2.rectangle(frame, (square_x1, square_y1), (square_x2, square_y2), (255,0,0), 2)#cube should be placed within this square
    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1) & 0xff
    if k==27:#ESC is pressed
        break
    elif k==32:#SPACE is pressed
        i += 1
        if (i==7):
            print("\n")
            check = color.count("*") 
            if check != 0:
                print("Rubik's initial state strings has an ERROR *! Please do it again!")
                break
            else:
                print("Rubik's initial state strings: \n", color)
                print("Solution: \n", solve(color))
                break
        else:
            if (i==1):
                print("U-Face Color: ")
            elif (i==2):
                print("R-Face Color: ")
            elif (i==3):
                print("F-Face Color: ")
            elif (i==4):
                print("D-Face Color: ")
            elif (i==5):
                print("L-Face Color: ")
            elif (i==6):
                print("B-Face Color: ")
            cube_roi=frame[square_y1:square_y2,square_x1:square_x2]
            color1 = one_side_color(cube_roi)
            color += color1
            print(color1)

cap.release()
cv2.destroyAllWindows()

