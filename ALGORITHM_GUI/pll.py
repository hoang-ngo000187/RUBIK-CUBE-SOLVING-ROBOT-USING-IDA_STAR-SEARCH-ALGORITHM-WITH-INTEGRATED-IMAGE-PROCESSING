from cube import Cube
#from cross import SOLVE_CROSS

 
str = [[["O", "B", "O"], ["G", "G", "G"], ["G", "G", "G"]],
       [["B", "G", "R"], ["O", "O", "O"], ["O", "O", "O"]],
       [["G", "O", "B"], ["B", "B", "B"], ["B", "B", "B"]],
       [["R", "B", "G"], ["R", "R", "R"], ["R", "R", "R"]],
       [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]],
       [["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]]]

#str = "OYBYGOWGOYWYWOGBGRBBGOBGYBOROWWRBGBRBYWRWRYOGWWRYYRGRO"
  
cb = Cube(str)
a = cb.__repr__()

def corner_GREEN_MAIN(cb):
    l = ""
    cb.move("R")
    cb.move("U")
    cb.move("RP")
    cb.move("UP")
    cb.move("RP")
    cb.move("F")
    cb.move("R2")
    cb.move("UP")
    cb.move("RP")
    cb.move("UP")
    cb.move("R")
    cb.move("U")
    cb.move("RP")
    cb.move("FP")
    l += "R U RP UP RP F R2 UP RP UP R U RP FP "
    a = cb.__repr__()
    return cb, l

def corner_ORANGE_MAIN(cb):
    l = ""
    cb.move("B")
    cb.move("U")
    cb.move("BP")
    cb.move("UP")
    cb.move("BP")
    cb.move("R")
    cb.move("B2")
    cb.move("UP")
    cb.move("BP")
    cb.move("UP")
    cb.move("B")
    cb.move("U")
    cb.move("BP")
    cb.move("RP")
    l += "B U BP UP BP R B2 UP BP UP B U BP RP "
    a = cb.__repr__()
    return cb, l

def corner_BLUE_MAIN(cb):
    l = ""
    cb.move("L")
    cb.move("U")
    cb.move("LP")
    cb.move("UP")
    cb.move("LP")
    cb.move("B")
    cb.move("L2")
    cb.move("UP")
    cb.move("LP")
    cb.move("UP")
    cb.move("L")
    cb.move("U")
    cb.move("LP")
    cb.move("BP")
    l += "L U LP UP LP B L2 UP LP UP L U LP BP "
    a = cb.__repr__()
    return cb, l

def corner_RED_MAIN(cb):
    l = ""
    cb.move("F")
    cb.move("U")
    cb.move("FP")
    cb.move("UP")
    cb.move("FP")
    cb.move("L")
    cb.move("F2")
    cb.move("UP")
    cb.move("FP")
    cb.move("UP")
    cb.move("F")
    cb.move("U")
    cb.move("FP")
    cb.move("LP")
    l += "F U FP UP FP L F2 UP FP UP F U FP LP "
    a = cb.__repr__()
    return cb, l

def corner(cb):
    a = cb.__repr__()
    list1 = ""
    # Cac cap goc khong trung mau
    if(a[0][0][0]!=a[0][0][2] and a[1][0][0]!=a[1][0][2] and
       a[2][0][0]!=a[2][0][2] and a[3][0][0]!=a[3][0][2]): # F R U' R' U' R U R' F' R U R' U' R' F R F'
        cb.move("F")
        cb.move("R")
        cb.move("UP")
        cb.move("RP")
        cb.move("UP")
        cb.move("R")
        cb.move("U")
        cb.move("RP")
        cb.move("FP")
        cb.move("R")
        cb.move("U")
        cb.move("RP")
        cb.move("UP")
        cb.move("RP")
        cb.move("F")
        cb.move("R")
        cb.move("FP")
        list1 += "F R UP RP UP R U RP FP R U RP UP RP F R FP "
        a = cb.__repr__()
        while True:
            if(a[0][0][0]== "G" and a[0][0][2] == "G" and 
               a[1][0][0]== "O" and a[1][0][2] == "O" and
               a[2][0][0]== "B" and a[2][0][2] == "B" and 
               a[3][0][0]== "R" and a[3][0][2]== "R"):
               break
           
            cb.move("U")
            a = cb.__repr__()
            list1 += "U "
    # GREEN
    elif(a[0][0][0] == "G" and a[0][0][2]=="G"):
        l = ""
        cb, l = corner_ORANGE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[0][0][0] == "O" and a[0][0][2]=="O"):
        l = ""
        cb.move("UP")
        list1 += "UP "
        cb, l = corner_BLUE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[0][0][0] == "B" and a[0][0][2]=="B"):
        l = ""
        cb.move("U2")
        list1 += "U2 "
        cb, l = corner_RED_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[0][0][0] == "R" and a[0][0][2]=="R"):
        l = ""
        cb.move("U")
        list1 += "U "
        cb, l = corner_GREEN_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    
    # ORANGE
    elif(a[1][0][0] == "G" and a[1][0][2]=="G"):
        l = ""
        cb.move("U")
        list1 += "U "
        cb, l = corner_ORANGE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[1][0][0] == "O" and a[1][0][2]=="O"):
        l = ""
        cb, l = corner_BLUE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[1][0][0] == "B" and a[1][0][2]=="B"):
        l = ""
        cb.move("UP")
        list1 += "UP "
        cb, l = corner_RED_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[1][0][0] == "R" and a[1][0][2]=="R"):
        l = ""
        cb.move("U2")
        list1 += "U2 "
        cb, l = corner_GREEN_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    
    # BLUE
    elif(a[2][0][0] == "G" and a[2][0][2]=="G"):
        l = ""
        cb.move("U2")
        list1 += "U2 "
        cb, l = corner_ORANGE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[2][0][0] == "O" and a[2][0][2]=="O"):
        l = ""
        cb.move("U")
        list1 += "U "
        cb, l = corner_BLUE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[2][0][0] == "B" and a[2][0][2]=="B"):
        l = ""
        cb, l = corner_RED_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[2][0][0] == "R" and a[2][0][2]=="R"):
        l = ""
        cb.move("UP")
        list1 += "UP "
        cb, l = corner_GREEN_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    
    # RED
    elif(a[3][0][0] == "G" and a[3][0][2]=="G"):
        l = ""
        cb.move("UP")
        list1 += "UP "
        cb, l = corner_ORANGE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[3][0][0] == "O" and a[3][0][2]=="O"):
        l = ""
        cb.move("U2")
        list1 += "U2 "
        cb, l = corner_BLUE_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[3][0][0] == "B" and a[3][0][2]=="B"):
        l = ""
        cb.move("U")
        list1 += "U "
        cb, l = corner_RED_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    elif(a[3][0][0] == "R" and a[3][0][2]=="R"):
        l = ""
        cb, l = corner_GREEN_MAIN(cb)
        list1 += l
        a = cb.__repr__()
    
    return cb, list1

def edge(cb):
    a = cb.__repr__()
    list2 = ""
    # th1: CANH DOI NHAU
    if(a[0][0][1]=="B" and a[1][0][1]=="R" and 
       a[2][0][1]=="G" and a[3][0][1]=="O"):
        # L2 R2 D' L2 R2 D2 L2 R2 D' L2 R2 U2 D2
        cb.move("L2")
        cb.move("R2")
        cb.move("DP")
        cb.move("L2")
        cb.move("R2")
        cb.move("D2")
        cb.move("L2")
        cb.move("R2")
        cb.move("DP")
        cb.move("L2")
        cb.move("R2")
        cb.move("U2")
        cb.move("D2")
        a = cb.__repr__()
        list2 += "L2 R2 DP L2 R2 D2 L2 R2 DP L2 R2 U2 D2 "
    # TH2: CANH KE NHAU
    elif(a[0][0][1]=="O" and a[1][0][1]=="G" and 
         a[2][0][1]=="R" and a[3][0][1]=="B"):
        # (L R') F' (L2 R2) BP (L2 R2) F' (L R') D2 (L2 R2) U
        cb.move("L")
        cb.move("RP")
        cb.move("FP")
        cb.move("L2")
        cb.move("R2")
        cb.move("BP")
        cb.move("L2")
        cb.move("R2")
        cb.move("FP")
        cb.move("L")
        cb.move("RP")
        cb.move("D2")
        cb.move("L2")
        cb.move("R2")
        cb.move("U")
        a = cb.__repr__()
        list2 += "L RP FP L2 R2 BP L2 R2 FP L RP D2 L2 R2 U "
    elif(a[0][0][1]=="R" and a[1][0][1]=="B" and 
         a[2][0][1]=="O" and a[3][0][1]=="G"):
        # L:B; R:F; F:L
        cb.move("B")
        cb.move("FP")
        cb.move("LP")
        cb.move("B2")
        cb.move("F2")
        cb.move("RP")
        cb.move("B2")
        cb.move("F2")
        cb.move("LP")
        cb.move("B")
        cb.move("FP")
        cb.move("D2")
        cb.move("B2")
        cb.move("F2")
        cb.move("U")
        a = cb.__repr__()
        list2 += "B FP LP B2 F2 RP B2 F2 LP B FP D2 B2 F2 U "
        # TH3: 1 mat da hoan thanh
        # Green
    elif(a[0][0][1]=="O" and a[2][0][1]=="B"): #Phai
        cb.move("R")
        cb.move("UP")
        cb.move("R")
        cb.move("U")
        cb.move("R")
        cb.move("U")
        cb.move("R")
        cb.move("UP")
        cb.move("RP")
        cb.move("UP")
        cb.move("R2")
        a = cb.__repr__()
        list2 += "R UP R U R U R UP RP UP R2 "
    elif(a[0][0][1]=="R" and a[2][0][1]=="B"): #Trai
        cb.move("R2")
        cb.move("U")
        cb.move("R")
        cb.move("U")
        cb.move("RP")
        cb.move("UP")
        cb.move("RP")
        cb.move("UP")
        cb.move("RP")
        cb.move("U")
        cb.move("RP")
        a = cb.__repr__()
        list2 += "R2 U R U RP UP RP UP RP U RP "
        # Orange
    elif(a[1][0][1]=="B" and a[3][0][1]=="R"): #Phai
        cb.move("B")
        cb.move("UP")
        cb.move("B")
        cb.move("U")
        cb.move("B")
        cb.move("U")
        cb.move("B")
        cb.move("UP")
        cb.move("BP")
        cb.move("UP")
        cb.move("B2")
        a = cb.__repr__()
        list2 += "B UP B U B U B UP BP UP B2 "
    elif(a[1][0][1]=="G" and a[2][0][1]=="R"): #Trai
        cb.move("B2")
        cb.move("U")
        cb.move("B")
        cb.move("U")
        cb.move("BP")
        cb.move("UP")
        cb.move("BP")
        cb.move("UP")
        cb.move("BP")
        cb.move("U")
        cb.move("BP")
        a = cb.__repr__()
        list2 += "B2 U B U BP UP BP UP BP U BP "
        # blue
    elif(a[2][0][1]=="R" and a[0][0][1]=="G"): #Phai
        cb.move("L")
        cb.move("UP")
        cb.move("L")
        cb.move("U")
        cb.move("L")
        cb.move("U")
        cb.move("L")
        cb.move("UP")
        cb.move("LP")
        cb.move("UP")
        cb.move("L2")
        a = cb.__repr__()
        list2 += "L UP L U L U L UP LP UP L2 "
    elif(a[2][0][1]=="O" and a[0][0][1]=="G"): #Trai
        cb.move("L2")
        cb.move("U")
        cb.move("L")
        cb.move("U")
        cb.move("LP")
        cb.move("UP")
        cb.move("LP")
        cb.move("UP")
        cb.move("LP")
        cb.move("U")
        cb.move("LP")
        a = cb.__repr__()
        list2 += "L2 U L U LP UP LP UP LP U LP "
        # RED
    elif(a[3][0][1]=="G" and a[1][0][1]=="O"): #Phai
        cb.move("F")
        cb.move("UP")
        cb.move("F")
        cb.move("U")
        cb.move("F")
        cb.move("U")
        cb.move("F")
        cb.move("UP")
        cb.move("FP")
        cb.move("UP")
        cb.move("F2")
        a = cb.__repr__()
        list2 += "F UP F U F U F UP FP UP F2 "
    elif(a[3][0][1]=="B" and a[1][0][1]=="O"): #Trai
        cb.move("F2")
        cb.move("U")
        cb.move("F")
        cb.move("U")
        cb.move("FP")
        cb.move("UP")
        cb.move("FP")
        cb.move("UP")
        cb.move("FP")
        cb.move("U")
        cb.move("FP")
        a = cb.__repr__()
        list2 += "F2 U F U FP UP FP UP FP U FP "
    return cb, list2

def PLL(cb):
    sol = ""
    a = cb.__repr__()
    if ((a[0][0][0] == a[0][0][1] == a[0][0][2]) and (a[1][0][0] == a[1][0][1] == a[1][0][2])
        and (a[2][0][0] == a[2][0][1] == a[2][0][2]) and (a[3][0][0] == a[3][0][1] == a[3][0][2])):
        while True:
            if(a[0][0][0] == "G"):
                break
            cb.move("U")
            a = cb.__repr__()
            sol += "U "
    else:
        cb1, sol1 = corner(cb)
        cb2, sol2 = edge(cb1)
        #print(cb2)
        sol = sol1 + sol2
        #print(sol)
    return cb, sol


        
        