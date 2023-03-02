from tkinter import * # đảm bảo dùng đủ hết thư viện
from tkinter.ttk import * # thư viện dùng cho combobox
from tkinter import messagebox
import tkinter as tk
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
import cv2
import PIL.Image, PIL.ImageTk # Thư viện dành riêng cho xử lý ảnh trên Tkinter
import serial
from __init1__ import solve, verify
from test_CB import solve_CB

from datetime import datetime
import time

from threading import Thread
# DRUDUURURUBLURULBFBFBRFRLLBBDDRDLDDRLBDLLDRFUFBFLBFUFF
# -------------------------------------------------------------------------------
red_hsv=[[159,78,130],[174,137,255]]
orange_hsv=[[6,46, 141],[15,175,217]]

white_hsv=[[126,45,82],[152,144,188]]
yellow_hsv=[[23,98, 127],[30,180,212]]
blue_hsv=[[92,73,73],[115,219,166]]
green_hsv=[[33,103,89],[53,210,174]]

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

running = False
# time variables initially set to 0
hours, minutes, seconds = 0, 0, 0

window = Tk()
window.title("BACHELOR THESIS - RUBIK’S CUBE SOLVING ROBOT USING IDA* SEARCH ALGORITHM WITH INTEGRATED IMAGE PROCESSING")
window.geometry('1200x750')
url = "http://192.168.0.3:4747/video"
# Đọc ảnh từ camera mặc định của máy tính
video = cv2.VideoCapture(0)

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
button_exit.place(x=470 + canvas_w, y=10)

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
#txt = Entry(window,width=50)
#txt.place(x=250 + canvas_w, y=100)


def update():
    # update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1000, update)          
    

"""
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
    timelb.config(text = minute + ':' + second)
    timelb.after(1000, timer_FC)
"""
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

    global running
    if not running:
        update()
        running = True

    data = txtsend.get('1.0', END) # TEXT, index1 = '1.0', index2 = END để lấy toàn bộ giá trị
    #action_str = xulychuoi(data)
    
    #data = data.replace(" ", "")
    while True:
        if(len(data) == BUFF_SIZE):
            break
        data+="|"
    data+= "\r\n"
    ser.write(data.encode())
    thread = Thread(target=pause)
    thread.start()

def pause():
    while True:
        receive = ser.readline()
        #receive_encode = receive.decode('utf8')
        if receive:
            break
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
        



def getsolve():
    global data
    if (var1.get() == 1) & (var2.get() == 0):
        data = txtSolu.get("1.0",'end-1c')
        #data = txtSolu.get('1.0', END)
    elif (var1.get() == 0) & (var2.get() == 1):
        data = txtSoluCB.get('1.0', END)
    else:
        data = ""
    data_xuly = xulychuoi(data)
    txtsend.insert('end', data_xuly)
    txtsend.config(state='disabled')
    

# Check box chọn giải thuật:
lblcheckbox = Label(window, text="Choose an method for robot to solve: ", font=("Arial Bold", 10))
lblcheckbox.place(x=75 + canvas_w, y=100)
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Kociemba Method',variable=var1, onvalue=1, offvalue=0, command=getsolve)
c1.place(x=75 + canvas_w, y=120)
c2 = tk.Checkbutton(window, text='Human Method',variable=var2, onvalue=1, offvalue=0, command=getsolve)
c2.place(x=75 + canvas_w, y=140)

# Nút nhấn gửi dữ liệu
btn = Button(window, text="Send data", command=send)
btn.place(x=250 + canvas_w, y=165)
 
 # TIMEr  
stopwatch_label = tk.Label(window, text = '00:00:00', font = ('ds-digital', 20, 'bold'), fg = "#f473b9", width = 10)
stopwatch_label.place(x=380 + canvas_w, y=175)
#timer_FC()


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
lblB = Label(window, text="D-Face Color State: ", font=("Arial Bold", 10))
lblB.place(x=50, y=canvas_h + 130)
txtB = Entry(window,width=30)
txtB.place(x=50, y=canvas_h + 150)

# Luu tru L string
lblL = Label(window, text="L-Face Color State: ", font=("Arial Bold", 10))
lblL.place(x=280, y=canvas_h + 130)
txtL = Entry(window,width=30)
txtL.place(x=280, y=canvas_h + 150)  

# Luu tru D string
lblD = Label(window, text="B-Face Color State: ", font=("Arial Bold", 10))
lblD.place(x=510, y=canvas_h + 130)
txtD = Entry(window,width=30)
txtD.place(x=510, y=canvas_h + 150)

# Luu tru chuoi trang thai ban dau string
lbl_str = Label(window, text="Rubik's initial state strings: ", font=("Arial Bold", 10))
lbl_str.place(x=50, y=canvas_h + 180)
txt_str = Entry(window,width=90)
txt_str.place(x=50, y=canvas_h + 200)

lblSolu = Label(window, text="Solution strings - Kociemba Method: ", font=("Arial Bold", 10))
lblSolu.place(x=canvas_w+75, y=canvas_h + 60)
txtSolu = Text(window,height=3, width=55)
txtSolu.place(x=canvas_w+75, y=canvas_h + 80)

lblSoluCB = Label(window, text="Solution strings - Human Method: ", font=("Arial Bold", 10))
lblSoluCB.place(x=canvas_w+75, y=canvas_h + 140)
txtSoluCB = Text(window,height=6, width=55)
txtSoluCB.place(x=canvas_w+75, y=canvas_h + 160)

# Textbox chứa số bước giải
txtNumSolu = Text(window,height = 1, width=20)
txtNumSolu.place(x=canvas_w+380, y=canvas_h + 60)
txtNumSoluCB = Text(window,height = 1, width=20)
txtNumSoluCB.place(x=canvas_w+380, y=canvas_h + 140)

lblsend = Label(window, text="Send String: ", font=("Arial Bold", 10))
lblsend.place(x=75 + canvas_w, y=170)
txtsend = Text(window, height = 2, width=30)
txtsend.place(x=75 + canvas_w, y=190)

solve_str = ""
# 
def btn_solve():
    global solve_str, data
    
    state = txt_str.get() # textbox lưu trạng thái đầu
    #state = txt.get()
    
    a = verify(state)
    if a == -1:
        print("each colour should appear exactly 9 times")
    elif a == -2:
        print("not all 12 edges exist exactly once")
    elif a == -3:
        print("flip error: one edge should be flipped")
    elif a == -4:
        print("not all corners exist exactly once")
    elif a == -5:
        print("twist error - a corner must be twisted")
    elif a == -6:
        print("Parity error - two corners or edges have to be exchanged")
    else:
    
        solve_str_Koci = solve(state)
        solve_list_Koci = solve_str_Koci.split(" ")
        numKoci = "Number of steps: " + str(len(solve_list_Koci))
        txtSolu.insert('end', solve_str_Koci)
        txtSolu.config(state='disabled')
        txtNumSolu.insert('end', numKoci)
        
        solve_str_CB = solve_CB(state)
        solve_list_CB = solve_str_CB.split(" ")
        numCB = "Number of steps: " + str(len(solve_list_CB))
        txtSoluCB.insert('end', solve_str_CB)
        txtSoluCB.config(state='disabled')
        txtNumSoluCB.insert('end', numCB)
    
btn_sol = Button(window, text="Solve", command=btn_solve)
btn_sol.place(x=610, y=canvas_h + 200)


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

    cv2.rectangle(frame, (square_x1, square_y1), (square_x2, square_y2), (0, 0, 0),
                  2)  # cube should be placed within this square
    
    
    square_img = frame_1[square_y1:square_y2, square_x1:square_x2]
    he, wi, _ = square_img.shape
    deltaL = he//3
    x1_1 = square_x1 + deltaL
    x1_2 = square_x1 + deltaL
    y1_1 = square_y1
    y1_2 = square_y1 + he
    cv2.line(frame, (x1_1, y1_1), (x1_2, y1_2), (0, 0, 0), 2)
    
    x2_1 = square_x1 + 2*deltaL
    x2_2 = square_x1 + 2*deltaL
    y2_1 = square_y1
    y2_2 = square_y1 + he
    cv2.line(frame, (x2_1, y2_1), (x2_2, y2_2), (0, 0, 0), 2)
    
    x3_1 = square_x1
    x3_2 = square_x1 + wi
    y3_1 = square_y1 + deltaL
    y3_2 = square_y1 + deltaL
    cv2.line(frame, (x3_1, y3_1), (x3_2, y3_2), (0, 0, 0), 2)
    
    x4_1 = square_x1
    x4_2 = square_x1 + wi
    y4_1 = square_y1 + 2*deltaL
    y4_2 = square_y1 + 2*deltaL
    cv2.line(frame, (x4_1, y4_1), (x4_2, y4_2), (0, 0, 0), 2)
    
    
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
                color1 = color1[:4] + "U" + color1[5:]
                drawU(color1)
                txtU.insert('end', color1)
                txtU.config(state='disabled')
            elif (i == 2):
                color1 = color1[:4] + "R" + color1[5:]
                drawR(color1)
                txtR.insert('end', color1)
                txtR.config(state='disabled')
            elif (i == 3):
                color1 = color1[:4] + "F" + color1[5:]
                drawF(color1)
                txtF.insert('end', color1)
                txtF.config(state='disabled')
            elif (i == 4):
                color1 = color1[:4] + "D" + color1[5:]
                drawD(color1)
                txtB.insert('end', color1)
                txtB.config(state='disabled')
            elif (i == 5):
                color1 = color1[:4] + "L" + color1[5:]
                drawL(color1)
                txtL.insert('end', color1)
                txtL.config(state='disabled')
            elif (i == 6):
                color1 = color1[:4] + "B" + color1[5:]
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
