from tkinter import * # đảm bảo dùng đủ hết thư viện
from tkinter.ttk import * # thư viện dùng cho combobox
from tkinter import messagebox
import tkinter as tk

import cv2
import PIL.Image, PIL.ImageTk # Thư viện dành riêng cho xử lý ảnh trên Tkinter
import serial
from __init1__ import solve

import time


# -------------------------------------------------------------------------------
red_hsv=[[147,50,100],[167,125,225]]
orange_hsv=[[0,78,121],[15,187,206]]
#white_hsv=[[101,27,123],[113,62,215]]
white_hsv=[[127,59,144],[146,168,196]]
yellow_hsv=[[21,75,118],[39,218,221]]
blue_hsv=[[97,125,116],[108,255,174]]
green_hsv=[[55,55,105],[74,203,162]]

def find_color(h,s,v):#finds color given h,s,v values(average)

    if (red_hsv[0][0]<=h<=red_hsv[1][0] and red_hsv[0][1]<=s<=red_hsv[1][1] and red_hsv[0][2]<=v<=red_hsv[1][2]):
        #cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
        #return "F"
        return "L"
    elif (orange_hsv[0][0]<=h<=orange_hsv[1][0] and orange_hsv[0][1] <= s <= orange_hsv[1][1] and orange_hsv[0][2]<=v<=orange_hsv[1][2]):
        #cv2.circle(img, (x, y), 2, (0, 69, 255), -1)
        #return "B"
        return "R"
    elif (yellow_hsv[0][0]<=h<=yellow_hsv[1][0] and yellow_hsv[0][1]<=s<=yellow_hsv[1][1] and yellow_hsv[0][2]<=v<=yellow_hsv[1][2]):
        #cv2.circle(img, (x, y), 2, (0, 191, 255), -1)
        #return "D"
        return "U"
    elif (green_hsv[0][0]<=h<=green_hsv[1][0] and green_hsv[0][1]<=s<=green_hsv[1][1] and green_hsv[0][2]<=v<=green_hsv[1][2]):
        #cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
        #return "L"
        return "F"
    elif (white_hsv[0][0]<=h<=white_hsv[1][0] and white_hsv[0][1]<=s<=white_hsv[1][1] and white_hsv[0][2]<=v<=white_hsv[1][2]):
        #cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        #return "U"
        return "D"
    elif (blue_hsv[0][0]<=h<=blue_hsv[1][0] and blue_hsv[0][1]<=s<=blue_hsv[1][1] and blue_hsv[0][2]<=v<=blue_hsv[1][2]):
        #cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
        #return "R"
        return "B"
    else:
        return '*'
    

def color_detection_function(x, y, hsv, delta):
    """

    """
    
    """
    pixel = hsv[x, y]

    hue = pixel[0]  # Lay gia tri Hue
    saturation = pixel[1]
    value = pixel[2]
    """
    
    dxy = delta   
    x_am = x - dxy
    x_duong = x + dxy
    y_am = y - dxy
    y_duong = y + dxy
    
    h= 0
    s = 0
    v = 0
    for i in range(x_am, x_duong + 1):
        for j in range(y_am, y_duong +1):
            pixel = hsv[i, j]
            h += pixel[0]
            s += pixel[1]
            v += pixel[2]
    
    hue = h//((x_duong +1 - x_am)*(y_duong +1 - y_am))
    saturation = s // ((x_duong +1 - x_am)*(y_duong +1 - y_am))
    value = v // ((x_duong +1 - x_am)*(y_duong +1 - y_am))
    
    
    #hue = pixel[0]  # Lay gia tri Hue
    #saturation = pixel[1]
    #value = pixel[2]

    color = find_color(hue, saturation, value)
    return color

 
def one_side_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    height, width, _ = image.shape
    delta = height // 9

    # pixel_1       pixel_2     pixel_3
    # pixel_4       pixel_5     pixel_6
    # pixel_7       pixel_8     pixel_9

    # Pick pixel_5
    x_5 = int(width / 2)
    y_5 = int(height / 2)
    color_5 = color_detection_function(x_5, y_5, hsv, delta)

    # Pick pixel_4
    x_4 = x_5
    y_4 = y_5 - 64
    color_4 = color_detection_function(x_4, y_4, hsv, delta)

    # Pick pixel_6
    x_6 = x_5
    y_6 = y_5 + 64
    color_6 = color_detection_function(x_6, y_6, hsv, delta)

    # Pick pixel_2
    x_2 = x_5 - 64
    y_2 = y_5
    color_2 = color_detection_function(x_2, y_2, hsv, delta)

    # Pick pixel_1
    x_1 = x_2
    y_1 = y_2 - 64
    color_1 = color_detection_function(x_1, y_1, hsv, delta)

    # Pick pixel_3
    x_3 = x_2
    y_3 = y_2 + 64
    color_3 = color_detection_function(x_3, y_3, hsv, delta)

    # Pick pixel_8
    x_8 = x_5 + 64
    y_8 = y_5
    color_8 = color_detection_function(x_8, y_8, hsv, delta)

    # Pick pixel_7
    x_7 = x_8
    y_7 = y_8 - 64
    color_7 = color_detection_function(x_7, y_7, hsv, delta)

    # Pick pixel_9
    x_9 = x_8
    y_9 = y_8 + 64
    color_9 = color_detection_function(x_9, y_9, hsv, delta)

    color = [color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8, color_9]
    color_side = "".join(str(x) for x in color)
    return color_side

# -------------------------------------------------------------------------------


window = Tk()
window.title("Robot Solve Rubik")
window.geometry('1200x750')
url = "http://192.168.0.3:4747/video"
# Đọc ảnh từ camera mặc định của máy tính
video = cv2.VideoCapture(url)

# Vùng canvas hiển thị video
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # lấy phân giải của camera chia đôi
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
canvas = Canvas(window, width = canvas_w, height = canvas_h)
canvas.place(x= 50, y=50)

# Vùng canvas hiển thị trạng thái Rubik
canvas_w1 = video.get(cv2.CAP_PROP_FRAME_WIDTH)//2 + 130  # lấy phân giải của camera chia đôi
canvas_h1 = video.get(cv2.CAP_PROP_FRAME_HEIGHT)//2
canvas1 = Canvas(window, width = canvas_w1, height = canvas_h1+50, bg = "#C0C0C0")
canvas1.place(x= 75 + canvas_w, y= canvas_h1)

lbl = Label(window, text="Get rubik's input state string from camera", font=("Arial Bold", 10))
lbl.place(x=canvas_w//2-100, y=25)



i = 0
color = ""
flag = False
flag_send = 0
ser = serial


def btn_connect():
    global ser, flag_send
    if (connect["text"] == "Connect"):
        connect.configure(text = "Disconnect")
        port_name = selected_com.get()
        baud_rate = selected_baud.get()
        ser  = serial.Serial(port_name, int(baud_rate), timeout = 0)

    elif (connect["text"] == "Disconnect"):
        connect.configure(text = "Connect")
        ser.close()

def btn_confirm():
    global i, flag
    i += 1
    flag = True

def btn_exit():
    video.release()
    window.destroy()

# Connect/Disconnect button
connect = Button(window, text="Connect", command=btn_connect)
connect.place(x=430 + canvas_w, y=67)

# Thêm 1 nut nhấn xác nhận
button = Button(window, text="CONFIRM", command=btn_confirm)
button.place(x=50 + canvas_w//2, y=canvas_h + 50)

# Thêm 1 nut nhấn giải thoát Camera
button_exit = Button(window, text="EXIT", command=btn_exit)
button_exit.place(x=75 + canvas_w, y=canvas_h1 - 100)

# Combo box hiển thị COM PORT
selected_com = StringVar()
com_label = Label(window, text = 'COM Port', font=("Arial Bold", 10))
com_label.place(x=75 + canvas_w, y=50)
port = Combobox(window, textvariable=selected_com, width = 20)
port['value'] = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6')
port.place(x=75 + canvas_w, y=70)

# # Combo box hiển thị Baud Rate
selected_baud = StringVar()
baud_label = Label(window, text = 'Baud Rate', font=("Arial Bold", 10))
baud_label.place(x=250 + canvas_w, y=50)
baud = Combobox(window, textvariable=selected_baud, width = 20)
baud['value'] = ('1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200')
baud.place(x=250 + canvas_w, y=70)

# Tạo 1 textbox nhập dữ liệu input
txt = Entry(window,width=50)
txt.place(x=250 + canvas_w, y=100)


def timer_FC():
    global second_num
    global minute_num
    if second_num < 59:
        second_num += 1
    else:
        second_num = 0
        if minute_num < 60:
            minute_num += 1

    if second_num < 10:
       second = '0' + str(second_num)
    else:
        second = str(second_num)
    if minute_num < 10:
        minute = '0' + str(minute_num)
    else:
        minute = str(minute_num)
    time.config(text = minute + ':' + second)
    time.after(1000, timer_FC)

second_num = 0
minute_num = 0

def xulychuoi(data):
    action = data.split(" ")

    for i in range(0, len(action)):
        if action[i] == "U'":
            action[i] = "u"
        elif action[i] == "U2":
            action[i] = "Z"
        
        elif action[i] == "R'":
            action[i] = "r"
        elif action[i] == "R2":
            action[i] = "X"
        
        elif action[i] == "F'":
            action[i] = "f"
        elif action[i] == "F2":
            action[i] = "C"
        
        elif action[i] == "B'":
            action[i] = "b"
        elif action[i] == "B2":
            action[i] = "V"
        
        elif action[i] == "L'":
            action[i] = "l"
        elif action[i] == "L2":
            action[i] = "N"
        
        elif action[i] == "D'":
            action[i] = "d"
        elif action[i] == "D2":
            action[i] = "M"
        else:
            action[i] = action[i]
    
    action_str = ""
    for i in range(0, len(action)):
        action_str += action[i]
    return action_str

def send():
    BUFF_SIZE = 30
    global ser, flag_send, second_num, minute_num
    second_num = 0
    minute_num = 0
     
    data = txtSolu.get('1.0', END) # TEXT, index1 = '1.0', index2 = END để lấy toàn bộ giá trị
    action_str = xulychuoi(data)
    
    #data = data.replace(" ", "")
    while True:
        if(len(action_str) == BUFF_SIZE):
            break
        action_str+="|"
    action_str += "\r\n"
    ser.write(action_str.encode())
    timer_FC()



# 
#btn = Button(window, text="Send data", command=send)
btn = Button(window, text="Send data", command=send)
btn.place(x=75 + canvas_w, y=100)


# Tạo 1 textbox nhập dữ liệu input
txt_state = Entry(window,width=50)
txt_state.place(x=250 + canvas_w, y=200)
    
timelb = tk.Label(window, text = '00:00', font = ('ds-digital', 40, 'bold'), fg = "#f473b9", width = 5)
timelb.place(x=380 + canvas_w, y=175)
    
# Luu tru U string
lblU = Label(window, text="U-Face Color State: ", font=("Arial Bold", 10))
lblU.place(x=50, y=canvas_h + 80)
txtU = Entry(window,width=30)
txtU.place(x=50, y=canvas_h + 100)

# Luu tru R string
lblR = Label(window, text="R-Face Color State: ", font=("Arial Bold", 10))
lblR.place(x=280, y=canvas_h + 80)
txtR = Entry(window,width=30)
txtR.place(x=280, y=canvas_h + 100)

# Luu tru F string
lblF = Label(window, text="F-Face Color State: ", font=("Arial Bold", 10))
lblF.place(x=510, y=canvas_h + 80)
txtF = Entry(window,width=30)
txtF.place(x=510, y=canvas_h + 100)

# Luu tru B string
lblB = Label(window, text="B-Face Color State: ", font=("Arial Bold", 10))
lblB.place(x=50, y=canvas_h + 130)
txtB = Entry(window,width=30)
txtB.place(x=50, y=canvas_h + 150)

# Luu tru L string
lblL = Label(window, text="L-Face Color State: ", font=("Arial Bold", 10))
lblL.place(x=280, y=canvas_h + 130)
txtL = Entry(window,width=30)
txtL.place(x=280, y=canvas_h + 150)  

# Luu tru D string
lblD = Label(window, text="D-Face Color State: ", font=("Arial Bold", 10))
lblD.place(x=510, y=canvas_h + 130)
txtD = Entry(window,width=30)
txtD.place(x=510, y=canvas_h + 150)

# Luu tru chuoi trang thai ban dau string
lbl_str = Label(window, text="Rubik's initial state strings: ", font=("Arial Bold", 10))
lbl_str.place(x=50, y=canvas_h + 180)
txt_str = Entry(window,width=107)
txt_str.place(x=50, y=canvas_h + 200)

lblSolu = Label(window, text="Solution strings: ", font=("Arial Bold", 10))
lblSolu.place(x=canvas_w+75, y=canvas_h + 80)
txtSolu = Text(window,height=8, width=55)
txtSolu.place(x=canvas_w+75, y=canvas_h + 100)

solve_str = ""
# 
def btn_solve():
    global solve_str
    #state = txt_state.get()
    state = txt_str.get()
    solve_str = solve(state)
    txtSolu.insert('end', solve_str)
    txtSolu.config(state='disabled')

btn_sol = Button(window, text="Solve", command=btn_solve)
btn_sol.place(x=250 + canvas_w, y=175)


photo = None

def fill_color(str_face, x1, y1 , x2, y2):
    if str_face == "D":
        canvas1.create_rectangle((x1, y1), (x2, y2), outline="black", fill="purple")
    elif str_face == "B":
        canvas1.create_rectangle((x1, y1), (x2, y2), outline="black", fill="blue")
    elif str_face == "L":
        canvas1.create_rectangle((x1, y1), (x2, y2), outline="black", fill="red")
    elif str_face == "R":
        canvas1.create_rectangle((x1, y1), (x2, y2), outline="black", fill="orange")
    elif str_face == "F":
        canvas1.create_rectangle((x1, y1), (x2, y2), outline="black", fill="green")
    elif str_face == "U":
        canvas1.create_rectangle((x1, y1), (x2, y2), outline="black", fill="yellow")

def drawU(color):
    #U = "".join(str(x) for x in color[0:9])
    U = color
    a = 0
    b = 0
    #U
    for i in range(90, 180, 30):
        a +=1
        b = 0
        for j in range(30, 90+10, 30):
            b += 1
            if a == 1 and b == 1:
                fill_color(U[0], i, j-30, i+30, j)
            elif a == 1 and b == 2:
                fill_color(U[3], i, j-30, i+30, j)
            elif a == 1 and b == 3:
                fill_color(U[6], i, j-30, i+30, j)
            elif a == 2 and b == 1:
                fill_color(U[1], i, j-30, i+30, j)
            elif a == 2 and b == 2:
                fill_color(U[4], i, j-30, i+30, j)
            elif a == 2 and b == 3:
                fill_color(U[7], i, j-30, i+30, j)
            elif a == 3 and b == 1:
                fill_color(U[2], i, j-30, i+30, j)
            elif a == 3 and b == 2:
                fill_color(U[5], i, j-30, i+30, j)
            elif a == 3 and b == 3:
                fill_color(U[8], i, j-30, i+30, j)
def drawR(color):
    #R = "".join(str(x) for x in color[9:18])
    R = color
    a = 0
    for i in range(180, 270, 30):
        a +=1
        b = 0
        for j in range(120, 180+10, 30):
            b += 1
            if a == 1 and b == 1:
                fill_color(R[0], i, j-30, i+30, j)
            elif a == 1 and b == 2:
                fill_color(R[3], i, j-30, i+30, j)
            elif a == 1 and b == 3:
                fill_color(R[6], i, j-30, i+30, j)
            elif a == 2 and b == 1:
                fill_color(R[1], i, j-30, i+30, j)
            elif a == 2 and b == 2:
                fill_color(R[4], i, j-30, i+30, j)
            elif a == 2 and b == 3:
                fill_color(R[7], i, j-30, i+30, j)
            elif a == 3 and b == 1:
                fill_color(R[2], i, j-30, i+30, j)
            elif a == 3 and b == 2:
                fill_color(R[5], i, j-30, i+30, j)
            elif a == 3 and b == 3:
                fill_color(R[8], i, j-30, i+30, j)

def drawF(color):
    #F = "".join(str(x) for x in color[18:27])
    F = color
    a = 0
    for i in range(90, 180, 30):
        a +=1
        b = 0
        for j in range(120, 180+10, 30):
            b += 1
            if a == 1 and b == 1:
                fill_color(F[0], i, j-30, i+30, j)
            elif a == 1 and b == 2:
                fill_color(F[3], i, j-30, i+30, j)
            elif a == 1 and b == 3:
                fill_color(F[6], i, j-30, i+30, j)
            elif a == 2 and b == 1:
                fill_color(F[1], i, j-30, i+30, j)
            elif a == 2 and b == 2:
                fill_color(F[4], i, j-30, i+30, j)
            elif a == 2 and b == 3:
                fill_color(F[7], i, j-30, i+30, j)
            elif a == 3 and b == 1:
                fill_color(F[2], i, j-30, i+30, j)
            elif a == 3 and b == 2:
                fill_color(F[5], i, j-30, i+30, j)
            elif a == 3 and b == 3:
                fill_color(F[8], i, j-30, i+30, j)
                
def drawD(color):
    #D = "".join(str(x) for x in color[27:36])
    D = color
    a = 0
    for i in range(90, 180, 30):
        a +=1
        b = 0
        for j in range(210, 270+10, 30):
            b += 1
            if a == 1 and b == 1:
                fill_color(D[0], i, j-30, i+30, j)
            elif a == 1 and b == 2:
                fill_color(D[3], i, j-30, i+30, j)
            elif a == 1 and b == 3:
                fill_color(D[6], i, j-30, i+30, j)
            elif a == 2 and b == 1:
                fill_color(D[1], i, j-30, i+30, j)
            elif a == 2 and b == 2:
                fill_color(D[4], i, j-30, i+30, j)
            elif a == 2 and b == 3:
                fill_color(D[7], i, j-30, i+30, j)
            elif a == 3 and b == 1:
                fill_color(D[2], i, j-30, i+30, j)
            elif a == 3 and b == 2:
                fill_color(D[5], i, j-30, i+30, j)
            elif a == 3 and b == 3:
                fill_color(D[8], i, j-30, i+30, j)

def drawL(color):
    # L = "".join(str(x) for x in color[36:45])
    L = color
    a = 0
    for i in range(0, 90, 30):
        a +=1
        b = 0
        for j in range(120, 180+10, 30):
            b += 1
            if a == 1 and b == 1:
                fill_color(L[0], i, j-30, i+30, j)
            elif a == 1 and b == 2:
                fill_color(L[3], i, j-30, i+30, j)
            elif a == 1 and b == 3:
                fill_color(L[6], i, j-30, i+30, j)
            elif a == 2 and b == 1:
                fill_color(L[1], i, j-30, i+30, j)
            elif a == 2 and b == 2:
                fill_color(L[4], i, j-30, i+30, j)
            elif a == 2 and b == 3:
                fill_color(L[7], i, j-30, i+30, j)
            elif a == 3 and b == 1:
                fill_color(L[2], i, j-30, i+30, j)
            elif a == 3 and b == 2:
                fill_color(L[5], i, j-30, i+30, j)
            elif a == 3 and b == 3:
                fill_color(L[8], i, j-30, i+30, j)

def drawB(color):
    #B = "".join(str(x) for x in color[45:])
    B = color
    a = 0
    for i in range(270, 360, 30):
        a +=1
        b = 0
        for j in range(120, 180+10, 30):
            b += 1
            if a == 1 and b == 1:
                fill_color(B[0], i, j-30, i+30, j)
            elif a == 1 and b == 2:
                fill_color(B[3], i, j-30, i+30, j)
            elif a == 1 and b == 3:
                fill_color(B[6], i, j-30, i+30, j)
            elif a == 2 and b == 1:
                fill_color(B[1], i, j-30, i+30, j)
            elif a == 2 and b == 2:
                fill_color(B[4], i, j-30, i+30, j)
            elif a == 2 and b == 3:
                fill_color(B[7], i, j-30, i+30, j)
            elif a == 3 and b == 1:
                fill_color(B[2], i, j-30, i+30, j)
            elif a == 3 and b == 2:
                fill_color(B[5], i, j-30, i+30, j)
            elif a == 3 and b == 3:
                fill_color(B[8], i, j-30, i+30, j)
    

    
def update_frame():
    global canvas, photo, color, flag, i
    # Đọc từ camera
    ret, frame = video.read()
    
    #Resize
    frame_1 = frame
    frame = cv2.resize(frame,dsize=None, fx=1, fy =1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # -----------------------------
    height, width, _ = frame.shape

    square_size_factor = 0.4  # fraction of height of image that square occupies
    square_x1 = int((width - ((square_size_factor) * height)) / 2)  # coordinate calculation for square corners
    square_x2 = int((width + ((square_size_factor) * height)) / 2)

    square_y1 = int(((1 - square_size_factor) / 2) * height)
    square_y2 = int(((1 + square_size_factor) / 2) * height)

    cv2.rectangle(frame, (square_x1, square_y1), (square_x2, square_y2), (0, 0, 255),
                  2)  # cube should be placed within this square
    
    
    square_img = frame_1[square_y1:square_y2, square_x1:square_x2]
    he, wi, _ = square_img.shape
    deltaL = he//3
    x1_1 = square_x1 + deltaL
    x1_2 = square_x1 + deltaL
    y1_1 = square_y1
    y1_2 = square_y1 + he
    cv2.line(frame, (x1_1, y1_1), (x1_2, y1_2), (0, 0, 255), 2)
    
    x2_1 = square_x1 + 2*deltaL
    x2_2 = square_x1 + 2*deltaL
    y2_1 = square_y1
    y2_2 = square_y1 + he
    cv2.line(frame, (x2_1, y2_1), (x2_2, y2_2), (0, 0, 255), 2)
    
    x3_1 = square_x1
    x3_2 = square_x1 + wi
    y3_1 = square_y1 + deltaL
    y3_2 = square_y1 + deltaL
    cv2.line(frame, (x3_1, y3_1), (x3_2, y3_2), (0, 0, 255), 2)
    
    x4_1 = square_x1
    x4_2 = square_x1 + wi
    y4_1 = square_y1 + 2*deltaL
    y4_2 = square_y1 + 2*deltaL
    cv2.line(frame, (x4_1, y4_1), (x4_2, y4_2), (0, 0, 255), 2)
    
    """
    square_img = frame_1[square_y1:square_y2, square_x1:square_x2]
    hsv_pic = cv2.cvtColor(square_img, cv2.COLOR_BGR2HSV)
    he, wi, _ = square_img.shape
    
    calib = he//10
    
    # Pick pixel_5
    x_4 = int(wi / 2)
    y_4 = int(he / 2)
    x4 = x_4 + (9*x_4)//4 + 2
    y4 = y_4 + (3*y_4)//2
    #pixel4 = hsv_pic[x_4,y_4]
    #cl4 = find_color(pixel4[0], pixel4[1], pixel4[2]) 
    cl4 = color_detection_function(x_4, y_4, hsv_pic, calib)
    if cl4 == "U":
        cv2.circle(frame, (x4, y4), 10, (255, 255, 255), -1)
    elif cl4 == "R":
        cv2.circle(frame, (x4, y4), 10, (255, 0, 0), -1)
    elif cl4 == "F":
        cv2.circle(frame, (x4, y4), 10, (0, 0, 255), -1)
    elif cl4 == "D":
        cv2.circle(frame, (x4, y4), 10, (255, 255, 0), -1)
    elif cl4 == "L":
        cv2.circle(frame, (x4, y4), 10, (0, 255, 0), -1)
    elif cl4 == "B":
        cv2.circle(frame, (x4, y4), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x4, y4), 10, (0, 0, 0), 2)
        
    # Pick pixel_4
    x_3 = x_4
    y_3 = y_4 - 64
    x3 = x_3 + (9*x_4)//4 + 2
    y3 = y_3 + (3*y_4)//2
    
    #pixel3 = hsv_pic[x_3,y_3]
    #cl3 = find_color(pixel3[0], pixel3[1], pixel3[2])
    cl3 = color_detection_function(x_3, y_3, hsv_pic, calib)
    if cl3 == "U":
        cv2.circle(frame, (x3, y3), 10, (255, 255, 255), -1)
    elif cl3 == "R":
        cv2.circle(frame, (x3, y3), 10, (255, 0, 0), -1)
    elif cl3 == "F":
        cv2.circle(frame, (x3, y3), 10, (0, 0, 255), -1)
    elif cl3 == "D":
        cv2.circle(frame, (x3, y3), 10, (255, 255, 0), -1)
    elif cl3 == "L":
        cv2.circle(frame, (x3, y3), 10, (0, 255, 0), -1)
    elif cl3 == "B":
        cv2.circle(frame, (x3, y3), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x3, y3), 10, (0, 0, 0), 2)
    
    

    # Pick pixel_6
    x_5 = x_4
    y_5 = y_4 + 64
    x5 = x_5 + (9*x_4)//4 + 2
    y5 = y_5 + (3*y_4)//2
    #pixel5 = hsv_pic[x_5,y_5]
    #cl5 = find_color(pixel5[0], pixel5[1], pixel5[2])
    cl5 = color_detection_function(x_5, y_5, hsv_pic, calib)
    if cl5 == "U":
        cv2.circle(frame, (x5, y5), 10, (255, 255, 255), -1)
    elif cl5 == "R":
        cv2.circle(frame, (x5, y5), 10, (255, 0, 0), -1)
    elif cl5 == "F":
        cv2.circle(frame, (x5, y5), 10, (0, 0, 255), -1)
    elif cl5 == "D":
        cv2.circle(frame, (x5, y5), 10, (255, 255, 0), -1)
    elif cl5 == "L":
        cv2.circle(frame, (x5, y5), 10, (0, 255, 0), -1)
    elif cl5 == "B":
        cv2.circle(frame,(x5, y5), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x5, y5), 10, (0, 0, 0), 2)

    # Pick pixel_2
    x_1 = x_4 - 64
    y_1 = y_4
    x1 = x_1 + (9*x_4)//4 + 2
    y1 = y_1 + (3*y_4)//2
    
    #pixel1 = hsv_pic[x_1, y_1]
    #cl1 = find_color(pixel1[0], pixel1[1], pixel1[2])
    cl1 = color_detection_function(x_1, y_1, hsv_pic, calib)
    if cl1 == "U":
        cv2.circle(frame, (x1, y1), 10, (255, 255, 255), -1)
    elif cl1 == "R":
        cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
    elif cl1 == "F":
        cv2.circle(frame, (x1, y1), 10, (0, 0, 255), -1)
    elif cl1 == "D":
        cv2.circle(frame, (x1, y1), 10, (255, 255, 0), -1)
    elif cl1 == "L":
        cv2.circle(frame, (x1, y1), 10, (0, 255, 0), -1)
    elif cl1 == "B":
        cv2.circle(frame, (x1, y1), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x1, y1), 10, (0, 0, 0), 2)

    # Pick pixel_1
    x_0 = x_1
    y_0 = y_1 - 64
    x0 = x_0 + (9*x_4)//4 + 2
    y0 = y_0 + (3*y_4)//2
    
    
    #pixel0 = hsv_pic[x_0, y_0]
    #cl0 = find_color(pixel0[0], pixel0[1], pixel0[2])
    
    cl0 = color_detection_function(x_0, y_0, hsv_pic, calib)
    if cl0 == "U":
        cv2.circle(frame, (x0, y0), 10, (255, 255, 255), -1)
    elif cl0 == "R":
        cv2.circle(frame, (x0, y0), 10, (255, 0, 0), -1)
    elif cl0 == "F":
        cv2.circle(frame, (x0, y0), 10, (0, 0, 255), -1)
    elif cl0 == "D":
        cv2.circle(frame, (x0, y0), 10, (255, 255, 0), -1)
    elif cl0 == "L":
        cv2.circle(frame, (x0, y0), 10, (0, 255, 0), -1)
    elif cl0 == "B":
        cv2.circle(frame, (x0, y0), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x0, y0), 10, (0, 0, 0), 2)
        
    # Pick pixel_3
    x_2 = x_1
    y_2 = y_1 + 64
    x2 = x_2 + (9*x_4)//4 + 2
    y2 = y_2 + (3*y_4)//2
    #pixel2 = hsv_pic[x_2, y_2]
    
    
    #cl2 = find_color(pixel2[0], pixel2[1], pixel2[2])
    cl2 = color_detection_function(x_2, y_2, hsv_pic, calib)
    if cl2 == "U":
        cv2.circle(frame, (x2, y2), 10, (255, 255, 255), -1)
    elif cl2 == "R":
        cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
    elif cl2 == "F":
        cv2.circle(frame, (x2, y2), 10, (0, 0, 255), -1)
    elif cl2 == "D":
        cv2.circle(frame, (x2, y2), 10, (255, 255, 0), -1)
    elif cl2 == "L":
        cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)
    elif cl2 == "B":
        cv2.circle(frame,(x2, y2), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x2, y2), 10, (0, 0, 0), 2)

    # Pick pixel_8
    x_7 = x_4 + 64
    y_7 = y_4
    x7 = x_7 + (9*x_4)//4 + 2
    y7 = y_7 + (3*y_4)//2
    
    #pixel7 = hsv_pic[x_7, y_7]
    #cl7 = find_color(pixel7[0], pixel7[1], pixel7[2])
    cl7 = color_detection_function(x_7, y_7, hsv_pic, calib)
    if cl7 == "U":
        cv2.circle(frame, (x7, y7), 10, (255, 255, 255), -1)
    elif cl7 == "R":
        cv2.circle(frame, (x7, y7), 10, (255, 0, 0), -1)
    elif cl7 == "F":
        cv2.circle(frame, (x7, y7), 10, (0, 0, 255), -1)
    elif cl7 == "D":
        cv2.circle(frame, (x7, y7), 10, (255, 255, 0), -1)
    elif cl7 == "L":
        cv2.circle(frame, (x7, y7), 10, (0, 255, 0), -1)
    elif cl7 == "B":
        cv2.circle(frame, (x7, y7), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x7, y7), 10, (0, 0, 0), 2)
    
    
    # Pick pixel_7
    x_6 = x_7
    y_6 = y_7 - 64
    x6 = x_6 + (9*x_4)//4 + 2
    y6 = y_6 + (3*y_4)//2 
    
    #pixel6 = hsv_pic[x_6, y_6]
    #cl6 = find_color(pixel6[0], pixel6[1], pixel6[2])
    cl6 = color_detection_function(x_6, y_6, hsv_pic, calib)
    if cl6 == "U":
        cv2.circle(frame, (x6, y6), 10, (255, 255, 255), -1)
    elif cl6 == "R":
        cv2.circle(frame, (x6, y6), 10, (255, 0, 0), -1)
    elif cl6 == "F":
        cv2.circle(frame, (x6, y6), 10, (0, 0, 255), -1)
    elif cl6 == "D":
        cv2.circle(frame, (x6, y6), 10, (255, 255, 0), -1)
    elif cl6 == "L":
        cv2.circle(frame, (x6, y6), 10, (0, 255, 0), -1)
    elif cl6 == "B":
        cv2.circle(frame, (x6, y6), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x6, y6), 10, (0, 0, 0), 2)
    
    # Pick pixel_9
    x_8 = x_7
    y_8 = y_7 + 64
    x8 = x_8 + (9*x_4)//4 + 2
    y8 = y_8 + (3*y_4)//2
    
    #pixel8 = hsv_pic[x_8,y_8]
    #cl8 = find_color(pixel8[0], pixel8[1], pixel8[2])
    cl8 = color_detection_function(x_8, y_8, hsv_pic, calib)
    if cl8 == "U":
        cv2.circle(frame, (x8, y8), 10, (255, 255, 255), -1)
    elif cl8 == "R":
        cv2.circle(frame, (x8, y8), 10, (255, 0, 0), -1)
    elif cl8 == "F":
        cv2.circle(frame, (x8, y8), 10, (0, 0, 255), -1)
    elif cl8 == "D":
        cv2.circle(frame, (x8, y8), 10, (255, 255, 0), -1)
    elif cl8 == "L":
        cv2.circle(frame, (x8, y8),10, (0, 255, 0), -1)
    elif cl8 == "B":
        cv2.circle(frame, (x8, y8), 10, (0, 69, 255), -1)
    else:
        cv2.circle(frame, (x8, y8), 10, (0, 0, 0), 2)
    
    """
    # Nut Confirm duoc nhan
    if flag == True:
        flag = False
        if (i == 7):
            check = color.count("*")
            if check != 0:
                #print("Rubik's initial state strings has an ERROR *! Please do it again!")
                txt_str.insert('end', "Rubik's initial state strings has an ERROR *! Please do it again!")
                txt_str.config(state='disabled')
                C = "UUUUUUUUURRRRRRRRRFFFFFFFFFBBBBBBBBBLLLLLLLLLDDDDDDDDD"
                #draw(C)
            else:
                txt_str.insert('end', color)
                txt_str.config(state='disabled')
                draw(color)
                #print("Rubik's initial state strings: \n", color)
                # print("Solution: \n", solve(color))
        else:
            if (i == 1):
                print("U-Face Color: ")
            elif (i == 2):
                print("R-Face Color: ")
            elif (i == 3):
                print("F-Face Color: ")
            elif (i == 4):
                print("D-Face Color: ")
            elif (i == 5):
                print("L-Face Color: ")
            elif (i == 6):
                print("B-Face Color: ")
            cube_roi = frame_1[square_y1:square_y2, square_x1:square_x2]
            color1 = one_side_color(cube_roi)
            if (i == 1):
                drawU(color1)
                txtU.insert('end', color1)
                txtU.config(state='disabled')
            elif (i == 2):
                drawR(color1)
                txtR.insert('end', color1)
                txtR.config(state='disabled')
            elif (i == 3):
                drawF(color1)
                txtF.insert('end', color1)
                txtF.config(state='disabled')
            elif (i == 4):
                drawD(color1)
                txtB.insert('end', color1)
                txtB.config(state='disabled')
            elif (i == 5):
                drawL(color1)
                txtL.insert('end', color1)
                txtL.config(state='disabled')
            elif (i == 6):
                drawB(color1)
                txtD.insert('end', color1)
                txtD.config(state='disabled')
            color += color1
            print(color1)


    # -----------------------------

    # frame đọc được từ camera là 1 array, ta convert array đó thành Image,
    # ... sau đó tiếp tục convert Image đó thành ImageTk
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    # nhét frame vào canvas để show lên
    canvas.create_image(0, 0, image = photo, anchor = tk.NW)
    window.after(5, update_frame) # update frame sau 15ms

update_frame()

window.mainloop()
