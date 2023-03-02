from cube import Cube
#from cross import SOLVE_CROSS

"""
str = [[["G", "Y", "G"], ["B", "G", "B"], ["G", "G", "G"]],
       [["O", "B", "R"], ["O", "O", "Y"], ["O", "O", "O"]],
       [["Y", "O", "Y"], ["R", "B", "O"], ["B", "B", "B"]],
       [["O", "G", "R"], ["G", "R", "R"], ["R", "R", "R"]],
       [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]],
       [["B", "Y", "B"], ["R", "Y", "Y"], ["Y", "G", "Y"]]]
"""

#str = "OYBYGOWGOYWYWOGBGRBBGOBGYBOROWWRBGBRBYWRWRYOGWWRYYRGRO"

cb = Cube(str)
a = cb.__repr__()

def check_edge_2ndfloor(cb):
    list1 = "" 
    a = cb.__repr__()
    
    while True:
        if((a[0][1][0]=="Y" or a[3][1][2]=="Y") and 
           (a[0][1][2]=="Y" or a[1][1][0]=="Y") and
           (a[1][1][2]=="Y" or a[2][1][0]=="Y") and
           (a[2][1][2]=="Y" or a[3][1][0]=="Y")):
            break
        
        while True:
            if(a[0][1][0]=="Y" or a[3][1][2]=="Y"): #ok
                break
            
            while True: 
                if(a[5][0][1]=="Y" or a[2][0][1]=="Y"):
                    break
                cb.move("U")
                list1 += "U "
                a = cb.__repr__()
                
            cb.move("F")
            cb.move("U")
            cb.move("FP")
            cb.move("UP")
            cb.move("LP")
            cb.move("UP")
            cb.move("L")
            list1 += "F U FP UP LP UP L "
            a = cb.__repr__()
        
        while True:
            if(a[0][1][2]=="Y" or a[1][1][0]=="Y"): #ok
                break
            
            while True: 
                if(a[5][1][0]=="Y" or a[3][0][1]=="Y"):
                    break
                cb.move("U")
                list1 += "U "
                a = cb.__repr__()
            cb.move("R")
            cb.move("U")
            cb.move("RP")
            cb.move("UP")
            cb.move("FP")
            cb.move("UP")
            cb.move("F")
            list1 += "R U RP UP FP UP F "
            a = cb.__repr__()
            
        while True:
            if(a[1][1][2]=="Y" or a[2][1][0]=="Y"): #ok
                break
            
            while True: 
                if(a[5][2][1]=="Y" or a[0][0][1]=="Y"):
                    break
                cb.move("U")
                list1 += "U "
                a = cb.__repr__()
            cb.move("B")
            cb.move("U")
            cb.move("BP")
            cb.move("UP")
            cb.move("RP")
            cb.move("UP")
            cb.move("R")
            list1 += "B U BP UP RP UP R "
            a = cb.__repr__()
        
        while True:
            if(a[2][1][2]=="Y" or a[3][1][0]=="Y"): # Y phải nằm ở vị trí a[5][1][2]
                break
            
            while True: 
                if(a[5][1][2]=="Y" or a[1][0][1]=="Y"):
                    break
                cb.move("U")
                list1 += "U "
                a = cb.__repr__()
            cb.move("L")
            cb.move("U")
            cb.move("LP")
            cb.move("UP")
            cb.move("BP")
            cb.move("UP")
            cb.move("B")
            list1 += "L U LP UP BP UP B "
            a = cb.__repr__()  
    return cb, list1

def solve_2nd(cb):
    a = cb.__repr__()
    list2 = ""
    
    while True:
        if(a[0][1][0]=="G" and a[0][1][2]=="G" and
           a[1][1][0]=="O" and a[1][1][2]=="O" and
           a[2][1][0]=="B" and a[2][1][2]=="B" and
           a[3][1][0]=="R" and a[3][1][2]=="R"):
            break
 
        # GREEN
        if(a[5][2][1]=="G" and a[0][0][1]=="R"): #ok
            cb.move("U2")
            cb.move("F")
            cb.move("U")
            cb.move("FP")
            cb.move("UP")
            cb.move("LP")
            cb.move("UP")
            cb.move("L")
            list2 += "U2 F U FP UP LP UP L "
            a = cb.__repr__()
            
        if(a[5][2][1]=="G" and a[0][0][1]=="O"): #OK
            cb.move("U2")
            cb.move("FP")
            cb.move("UP")
            cb.move("F")
            cb.move("U")
            cb.move("R")
            cb.move("U")
            cb.move("RP")
            list2 += "U2 FP UP F U R U RP "
            a = cb.__repr__()
            
        # ORANGE
        if(a[5][2][1]=="O" and a[0][0][1]=="B"): #ok
            cb.move("U")
            cb.move("RP")
            cb.move("UP")
            cb.move("R")
            cb.move("U")
            cb.move("B")
            cb.move("U")
            cb.move("BP")
            list2 += "U RP UP R U B U BP "
            a = cb.__repr__()
            
        if(a[5][2][1]=="O" and a[0][0][1]=="G"): #ok
            cb.move("U")
            cb.move("R")
            cb.move("U")
            cb.move("RP")
            cb.move("UP")
            cb.move("FP")
            cb.move("UP")
            cb.move("F")
            list2 += "U R U RP UP FP UP F "
            a = cb.__repr__()
            
        #BLUE
        if(a[5][2][1]=="B" and a[0][0][1]=="O"): #ok
            cb.move("B")
            cb.move("U")
            cb.move("BP")
            cb.move("UP")
            cb.move("RP")
            cb.move("UP")
            cb.move("R")
            list2 += "B U BP UP RP UP R "
            a = cb.__repr__()
            
        if(a[5][2][1]=="B" and a[0][0][1]=="R"): #ok
            cb.move("BP")
            cb.move("UP")
            cb.move("B")
            cb.move("U")
            cb.move("L")
            cb.move("U")
            cb.move("LP")
            list2 += "BP UP B U L U LP "
            a = cb.__repr__()
        
            
        # RED
        if(a[5][2][1]=="R" and a[0][0][1]=="B"):#ok
            cb.move("UP")
            cb.move("L")
            cb.move("U")
            cb.move("LP")
            cb.move("UP")
            cb.move("BP")
            cb.move("UP")
            cb.move("B")
            list2 += "UP L U LP UP BP UP B "
            a = cb.__repr__()
            
        if(a[5][2][1]=="R" and a[0][0][1]=="G"): #ok
            cb.move("UP")
            cb.move("LP")
            cb.move("UP")
            cb.move("L")
            cb.move("U")
            cb.move("F")
            cb.move("U")
            cb.move("FP")
            list2 += "UP LP UP L U F U FP "
            a = cb.__repr__()
            
        if(a[5][2][1]=="Y" or a[0][0][1]=="Y"):
            cb.move("U")
            list2 += "U "
            a = cb.__repr__()
            
    return cb, list2

def solve_list(sol):
    sol_replace = sol.replace("U U U ", "UP ")
    sol_replace = sol_replace.replace("U U ", "U2 ")
    sol_replace = sol_replace.replace("U UP", "")
    return sol_replace
    
def FLOOR_2ND(cb):
    a = cb.__repr__()
    cb1, sol1 = check_edge_2ndfloor(cb)
    cb2, sol2 = solve_2nd(cb1)
    sol = sol1 + sol2
    sol = solve_list(sol)
    #print(cb2)
    #print(sol)
    return cb, sol





    
        