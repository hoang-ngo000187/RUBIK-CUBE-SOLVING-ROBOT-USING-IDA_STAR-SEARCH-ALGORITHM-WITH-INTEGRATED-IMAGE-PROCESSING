from cube import Cube
from cross import SOLVE_CROSS

 
str = [[["B", "R", "Y"], ["Y", "G", "O"], ["W", "W", "Y"]],
       [["R", "W", "Y"], ["G", "O", "W"], ["B", "Y", "Y"]],
       [["G", "Y", "G"], ["G", "B", "R"], ["R", "Y", "W"]],
       [["W", "O", "W"], ["B", "R", "B"], ["R", "R", "R"]],
       [["B", "B", "O"], ["G", "W", "O"], ["G", "G", "B"]],
       [["O", "R", "O"], ["B", "Y", "O"], ["O", "W", "G"]]]

#str = "OYBYGOWGOYWYWOGBGRBBGOBGYBOROWWRBGBRBYWRWRYOGWWRYYRGRO"
 
cb = Cube(str)
a = cb.__repr__()

def check_W_edge(cb): # kiểm tra lop duoi cung có W không
    a = cb.__repr__()
    list1 = ""
    
    if (a[4][0][0] == "W") and (a[0][2][0] != "G" or a[3][2][2] != "R"):
        cb.move("LP")
        cb.move("U")
        cb.move("L")
        list1 += "LP U L "
        a = cb.__repr__()
    
    if (a[4][0][2] == "W") and (a[0][2][2] != "G" or a[1][2][0] != "O"):
        cb.move("R")
        cb.move("U")
        cb.move("RP")
        list1 += "R U RP "
        a = cb.__repr__()

    if (a[4][2][2] == "W") and (a[1][2][2] != "O" or a[2][2][0] != "B"):
        cb.move("B")
        cb.move("U")
        cb.move("BP")
        list1 += "B U BP "
        a = cb.__repr__()

    if (a[4][2][0] == "W") and (a[2][2][2] != "B" or a[3][2][0] != "R"):
        cb.move("L")
        cb.move("U")
        cb.move("LP")
        list1 += "L U LP "
        a = cb.__repr__()
    
    return cb, list1
        
#check_W_edge(cb)

def check_W_edge_DOWN(cb): # white nằm ở X7 or X9 (X=F, R, B, L)
    a = cb.__repr__()
    list2 = ""
    # GREEN
    if(a[0][2][0]=="W"):
        while True:
            if(a[0][0][2]!="W" and a[5][2][2]!="W" and a[1][0][0]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("LP")
        cb.move("U")
        cb.move("L")
        list2 += "LP U L "
        a = cb.__repr__()
    
    if(a[0][2][2]=="W"):
        while True:
            if(a[0][0][0]!="W" and a[3][0][2]!="W" and a[5][2][0]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("R")
        cb.move("UP")
        cb.move("RP")
        list2 += "R UP RP "
        a = cb.__repr__()
        
    # ORANGE
    if(a[1][2][0]=="W"):
        while True:
            if(a[1][0][2]!="W" and a[5][0][2]!="W" and a[2][0][0]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("FP")
        cb.move("U")
        cb.move("F")
        list2 += "FP U F "
        a = cb.__repr__()
    
    if(a[1][2][2]=="W"):
        while True:
            if(a[1][0][0]!="W" and a[0][0][2]!="W" and a[5][2][2]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("B")
        cb.move("UP")
        cb.move("BP")
        list2 += "B UP BP "
        a = cb.__repr__()
    
    # BLUE
    if(a[2][2][0]=="W"):
        while True:
            if(a[2][0][2]!="W" and a[5][0][0]!="W" and a[3][0][0]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("RP")
        cb.move("U")
        cb.move("R")
        list2 += "RP U R "
        a = cb.__repr__()
    
    if(a[2][2][2]=="W"):
        while True:
            if(a[2][0][0]!="W" and a[1][0][2]!="W" and a[5][0][2]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("L")
        cb.move("UP")
        cb.move("LP")
        list2 += "L UP LP "
        a = cb.__repr__()
    
    # RED
    if(a[3][2][0]=="W"):
        while True:
            if(a[3][0][2]!="W" and a[5][2][0]!="W" and a[0][0][0]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("BP")
        cb.move("U")
        cb.move("B")
        list2 += "BP U B "
        a = cb.__repr__()
    
    if(a[3][2][2]=="W"):
        while True:
            if(a[3][0][0]!="W" and a[5][0][0]!="W" and a[2][0][2]!="W"):
                break
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
        cb.move("F")
        cb.move("UP")
        cb.move("FP")
        list2 += "F UP FP "
        a = cb.__repr__()
    
    return cb, list2

def match(cb):
    a = cb.__repr__()
    list3 = ""
    while True:
        if (a[0][0][0]!="W" and a[0][0][2]!="W" and
            a[1][0][0]!="W" and a[1][0][2]!="W" and
            a[2][0][0]!="W" and a[2][0][2]!="W" and
            a[3][0][0]!="W" and a[3][0][2]!="W"
            ):
            break
        #GREEN
        if(a[0][0][0]=="W"):
            if(a[5][2][0]=="G"):
                cb.move("UP")
                cb.move("LP")
                cb.move("U")
                cb.move("L")
                list3 += "UP LP U L "
                a = cb.__repr__()
            elif(a[5][2][0]=="O"):
                cb.move("U2")
                cb.move("FP")
                cb.move("U")
                cb.move("F")
                list3 += "U2 FP U F "
                a = cb.__repr__()
            elif(a[5][2][0]=="B"):
                cb.move("U")
                cb.move("RP")
                cb.move("U")
                cb.move("R")
                list3 += "U RP U R "
                a = cb.__repr__()
            elif(a[5][2][0]=="R"):
                cb.move("BP")
                cb.move("U")
                cb.move("B")
                list3 += "BP U B "
                a = cb.__repr__()
        
        if(a[0][0][2]=="W"):
            if(a[5][2][2]=="G"):
                cb.move("U")
                cb.move("R")
                cb.move("UP")
                cb.move("RP")
                list3 += "U R UP RP "
                a = cb.__repr__()
            elif(a[5][2][2]=="O"):
                cb.move("B")
                cb.move("UP")
                cb.move("BP")
                list3 += "B UP BP "
                a = cb.__repr__()
            elif(a[5][2][2]=="B"):
                cb.move("UP")
                cb.move("R")
                cb.move("UP")
                cb.move("RP")
                list3 += "UP R UP RP "
                a = cb.__repr__()
            elif(a[5][2][2]=="R"):
                cb.move("U2")
                cb.move("F")
                cb.move("UP")
                cb.move("FP")
                list3 += "U2 F UP FP "
                a = cb.__repr__()
        
        #ORANGE
        if(a[1][0][0]=="W"):
            if(a[5][2][2]=="G"):
                cb.move("LP")
                cb.move("U")
                cb.move("L")
                list3 += "LP U L "
                a = cb.__repr__()
            elif(a[5][2][2]=="O"):
                cb.move("UP")
                cb.move("FP")
                cb.move("U")
                cb.move("F")
                list3 += "UP FP U F "
                a = cb.__repr__()
            elif(a[5][2][2]=="B"):
                cb.move("U2")
                cb.move("RP")
                cb.move("U")
                cb.move("R")
                list3 += "U2 RP U R "
                a = cb.__repr__()
            elif(a[5][2][2]=="R"):
                cb.move("U")
                cb.move("BP")
                cb.move("U")
                cb.move("B")
                list3 += "U BP U B "
                a = cb.__repr__()
        
        if(a[1][0][2]=="W"):
            if(a[5][0][2]=="G"):
                cb.move("U2")
                cb.move("R")
                cb.move("UP")
                cb.move("RP")
                list3 += "U2 R UP RP "
                a = cb.__repr__()
            elif(a[5][0][2]=="O"):
                cb.move("U")
                cb.move("B")
                cb.move("UP")
                cb.move("BP")
                list3 += "U B UP BP "
                a = cb.__repr__()
            elif(a[5][0][2]=="B"):
                cb.move("L")
                cb.move("UP")
                cb.move("LP")
                list3 += "L UP LP "
                a = cb.__repr__()
            elif(a[5][0][2]=="R"):
                cb.move("UP")
                cb.move("F")
                cb.move("UP")
                cb.move("FP")
                list3 += "UP F UP FP "
                a = cb.__repr__()
        
        #BLUE
        if(a[2][0][0]=="W"):
            if(a[5][0][2]=="G"):
                cb.move("U")
                cb.move("LP")
                cb.move("U")
                cb.move("L")
                list3 += "U LP U L "
                a = cb.__repr__()
            elif(a[5][0][2]=="O"):
                cb.move("FP")
                cb.move("U")
                cb.move("F")
                list3 += "FP U F "
                a = cb.__repr__()
            elif(a[5][0][2]=="B"):
                cb.move("UP")
                cb.move("RP")
                cb.move("U")
                cb.move("R")
                list3 += "UP RP U R "
                a = cb.__repr__()
            elif(a[5][0][2]=="R"):
                cb.move("U2")
                cb.move("BP")
                cb.move("U")
                cb.move("B")
                list3 += "U2 BP U B "
                a = cb.__repr__()
        
        if(a[2][0][2]=="W"):
            if(a[5][0][0]=="G"):
                cb.move("UP")
                cb.move("R")
                cb.move("UP")
                cb.move("RP")
                list3 += "UP R UP RP "
                a = cb.__repr__()
            elif(a[5][0][0]=="O"):
                cb.move("U2")
                cb.move("B")
                cb.move("UP")
                cb.move("BP")
                list3 += "U2 B UP BP "
                a = cb.__repr__()
            elif(a[5][0][0]=="B"):
                cb.move("U")
                cb.move("L")
                cb.move("UP")
                cb.move("LP")
                list3 += "U L UP LP "
                a = cb.__repr__()
            elif(a[5][0][0]=="R"):
                cb.move("F")
                cb.move("UP")
                cb.move("FP")
                list3 += "F UP FP "
                a = cb.__repr__()
        #RED
        if(a[3][0][0]=="W"):
            if(a[5][0][0]=="G"):
                cb.move("U2")
                cb.move("LP")
                cb.move("U")
                cb.move("L")
                list3 += "U2 LP U L "
                a = cb.__repr__()
            elif(a[5][0][0]=="O"):
                cb.move("U")
                cb.move("FP")
                cb.move("U")
                cb.move("F")
                list3 += "U FP U F "
                a = cb.__repr__()
            elif(a[5][0][0]=="B"):
                cb.move("RP")
                cb.move("U")
                cb.move("R")
                list3 += "RP U R "
                a = cb.__repr__()
            elif(a[5][0][0]=="R"):
                cb.move("UP")
                cb.move("BP")
                cb.move("U")
                cb.move("B")
                list3 += "UP BP U B "
                a = cb.__repr__()
        
        if(a[3][0][2]=="W"):
            if(a[5][2][0]=="G"):
                cb.move("R")
                cb.move("UP")
                cb.move("RP")
                list3 += "R UP RP "
                a = cb.__repr__()
            elif(a[5][2][0]=="O"):
                cb.move("UP")
                cb.move("B")
                cb.move("UP")
                cb.move("BP")
                list3 += "UP B UP BP "
                a = cb.__repr__()
            elif(a[5][2][0]=="B"):
                cb.move("U2")
                cb.move("L")
                cb.move("UP")
                cb.move("LP")
                list3 += "U2 L UP LP "
                a = cb.__repr__()
            elif(a[5][2][0]=="R"):
                cb.move("U")
                cb.move("F")
                cb.move("UP")
                cb.move("FP")
                list3 += "U F UP FP "
                a = cb.__repr__()
        
    return cb, list3
x = ""
def check_W_edge_UP(cb):
    global x
    a = cb.__repr__()
    list4 = ""
    while True:
        if(a[5][0][0]!="W" and a[5][0][2]!="W" and a[5][2][0]!="W" and a[5][2][2]!="W"):
            break
        #GREEN
        
        if (a[5][2][0]=="W"):
            if (a[4][0][0]!="W"):
                x = ""
                cb.move("UP")
                cb.move("LP")
                cb.move("U2")
                cb.move("L")
                list4 += "UP LP U2 L "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][0][2]!="W"):
                x = ""
                cb.move("U2")
                cb.move("FP")
                cb.move("U2")
                cb.move("F")
                list4 += "U2 FP U2 F "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][2]!="W"):
                x = ""
                cb.move("UP")
                cb.move("B")
                cb.move("U2")
                cb.move("BP")
                list4 += "UP B U2 BP "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][0]!="W"):
                x = ""
                cb.move("BP")
                cb.move("U2")
                cb.move("B")
                list4 += "BP U2 B "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
        if (a[5][2][2]=="W"):
            if (a[4][0][0]!="W"):
                x = ""
                cb.move("LP")
                cb.move("U2")
                cb.move("L")
                list4 += "LP U2 L "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][0][2]!="W"):
                x = ""
                cb.move("U")
                cb.move("R")
                cb.move("U2")
                cb.move("RP")
                list4 += "U R U2 RP "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][2]!="W"):
                x = ""
                cb.move("B")
                cb.move("U2")
                cb.move("BP")
                list4 += "B U2 BP "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][0]!="W"):
                x = ""
                cb.move("BP")
                cb.move("UP")
                cb.move("B")
                list4 += "BP UP B "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
        
        if (a[5][0][0]=="W"):
            if (a[4][0][0]!="W"):
                x = ""
                cb.move("U")
                cb.move("LP")
                cb.move("UP")
                cb.move("L")
                list4 += "U LP UP L "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
                
            elif (a[4][0][2]!="W"):
                x = ""
                cb.move("R")
                cb.move("U")
                cb.move("RP")
                list4 += "R U RP "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][2]!="W"):
                x = ""
                cb.move("UP")
                cb.move("B")
                cb.move("U")
                cb.move("BP")
                list4 += "UP B U BP "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][0]!="W"):
                x = ""
                cb.move("UP")
                cb.move("BP")
                cb.move("U2")
                cb.move("B")
                list4 += "UP BP U2 B "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
        
        if (a[5][0][2]=="W"):
            if (a[4][0][0]!="W"):
                x = ""
                cb.move("LP")
                cb.move("UP")
                cb.move("L")
                list4 += "LP UP L "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][0][2]!="W"):
                x = ""
                cb.move("UP")
                cb.move("R")
                cb.move("U")
                cb.move("RP")
                list4 += "UP R U RP "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][2]!="W"):
                x = ""
                cb.move("U")
                cb.move("B")
                cb.move("U2")
                cb.move("BP")
                list4 += "U B U2 BP "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
            elif (a[4][2][0]!="W"):
                x = ""
                cb.move("U")
                cb.move("BP")
                cb.move("UP")
                cb.move("B")
                list4 += "U BP UP B "
                a = cb.__repr__()
                cb, x = match(cb)
                list4 += x
                a = cb.__repr__()
        
            
    return cb, list4

        
            

def T(cb):
    a = cb.__repr__()
    #cb0, sol0 = SOLVE_CROSS(cb)
    
    cb1,sol1 = check_W_edge(cb)
    
    cb2,sol2 = check_W_edge_DOWN(cb1)
    
    cb3,sol3 = match(cb2)
    
    cb4,sol4 = check_W_edge_UP(cb3)
    
    #cb5,sol5 = match(cb4)
    sol = sol1+sol2+sol3+sol4
    sol_replace=sol.replace("U U U ", "UP ")
    sol_replace=sol_replace.replace("U U ", "U2 ")
    
    
    return cb, sol_replace


        