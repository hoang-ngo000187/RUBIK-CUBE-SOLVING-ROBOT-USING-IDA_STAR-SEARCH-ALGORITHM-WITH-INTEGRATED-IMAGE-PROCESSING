from cube import Cube
#from cross import SOLVE_CROSS

 
str = [[["Y", "Y", "O"], ["G", "G", "G"], ["G", "G", "G"]],
       [["Y", "Y", "R"], ["O", "O", "O"], ["O", "O", "O"]],
       [["G", "Y", "R"], ["B", "B", "B"], ["B", "B", "B"]],
       [["Y", "Y", "B"], ["R", "R", "R"], ["R", "R", "R"]],
       [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]],
       [["B", "O", "Y"], ["R", "Y", "B"], ["O", "G", "G"]]]

#str = "OYBYGOWGOYWYWOGBGRBBGOBGYBOROWWRBGBRBYWRWRYOGWWRYYRGRO"
  
cb = Cube(str)
a = cb.__repr__()

def cross_UP(cb):
    a = cb.__repr__()
    list1 = ""
    while True:
        if(a[5][0][1]=="Y" and a[5][1][0]=="Y" and a[5][1][2]=="Y" and a[5][2][1]=="Y"):
            break
        # TH1: dau gach ngang
        if(a[5][1][0]=="Y" and a[5][1][2]=="Y"):
            cb.move("F")
            cb.move("R")
            cb.move("U")
            cb.move("RP")
            cb.move("UP")
            cb.move("FP")
            list1 += "F R U RP UP FP "
            a = cb.__repr__()
        elif(a[5][0][1]=="Y" and a[5][2][1]=="Y"):
            cb.move("L")
            cb.move("F")
            cb.move("U")
            cb.move("FP")
            cb.move("UP")
            cb.move("LP")
            list1 += "L F U FP UP LP "
            a = cb.__repr__()
        #TH2: Chu L nho
        elif(a[5][1][2]=="Y" and a[5][2][1]=="Y"):
            cb.move("B")
            cb.move("U")
            cb.move("L")
            cb.move("UP")
            cb.move("LP")
            cb.move("BP")
            list1 += "B U L UP LP BP "
            a = cb.__repr__()
        elif(a[5][1][2]=="Y" and a[5][0][1]=="Y"):
            cb.move("L")
            cb.move("U")
            cb.move("F")
            cb.move("UP")
            cb.move("FP")
            cb.move("LP")
            list1 += "L U F UP FP LP "
            a = cb.__repr__()
        elif(a[5][0][1]=="Y" and a[5][1][0]=="Y"):
            cb.move("F")
            cb.move("U")
            cb.move("R")
            cb.move("UP")
            cb.move("RP")
            cb.move("FP")
            list1 += "F U R UP RP FP "
            a = cb.__repr__()
        elif(a[5][2][1]=="Y" and a[5][1][0]=="Y"):
            cb.move("R")
            cb.move("U")
            cb.move("B")
            cb.move("UP")
            cb.move("BP")
            cb.move("RP")
            list1 += "R U B UP BP RP "
            a = cb.__repr__()
        else:
            cb.move("F")
            cb.move("R")
            cb.move("U")
            cb.move("RP")
            cb.move("UP")
            cb.move("FP")
            cb.move("B")
            cb.move("U")
            cb.move("L")
            cb.move("UP")
            cb.move("LP")
            cb.move("BP")
            list1 += "F R U RP UP FP B U L UP LP BP "
            a = cb.__repr__()
    return cb, list1

def full_UP(cb):
    a = cb.__repr__()
    list2 = ""
    
    
    while True:
        if(a[5][0][0]=="Y" and a[5][0][1]=="Y" and a[5][0][2]=="Y" and
           a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
           a[5][2][0]=="Y" and a[5][2][1]=="Y" and a[5][2][2]=="Y"):
            break
        
        #TH1: 
        # GREEN
        if(a[5][0][0]!="Y" and a[5][0][2]!="Y" and a[5][2][2]!="Y" and
           a[0][0][2]=="Y" and a[1][0][2]=="Y" and a[2][0][2]=="Y"):
            cb.move("R")
            cb.move("U")
            cb.move("RP")
            cb.move("U")
            cb.move("R")
            cb.move("U2")
            cb.move("RP")
            list2 += "R U RP U R U2 RP "
            a = cb.__repr__()
        
        # ORANGE
        elif(a[5][0][0]!="Y" and a[5][0][2]!="Y" and a[5][2][0]!="Y" and
           a[1][0][2]=="Y" and a[2][0][2]=="Y" and a[3][0][2]=="Y"):
            cb.move("B")
            cb.move("U")
            cb.move("BP")
            cb.move("U")
            cb.move("B")
            cb.move("U2")
            cb.move("BP")
            list2 += "B U BP U B U2 BP "
            a = cb.__repr__()
        
        # blue
        elif(a[5][0][0]!="Y" and a[5][2][0]!="Y" and a[5][2][2]!="Y" and
           a[2][0][2]=="Y" and a[3][0][2]=="Y" and a[0][0][2]=="Y"):
            cb.move("L")
            cb.move("U")
            cb.move("LP")
            cb.move("U")
            cb.move("L")
            cb.move("U2")
            cb.move("LP")
            list2 += "L U LP U L U2 LP "
            a = cb.__repr__()
        
        # RED
        elif(a[5][0][2]!="Y" and a[5][2][0]!="Y" and a[5][2][2]!="Y" and
           a[3][0][2]=="Y" and a[0][0][2]=="Y" and a[1][0][2]=="Y"):
            cb.move("F")
            cb.move("U")
            cb.move("FP")
            cb.move("U")
            cb.move("F")
            cb.move("U2")
            cb.move("FP")
            list2 += "F U FP U F U2 FP "
            a = cb.__repr__()
        
        # TH2: #############################    
        #GREEN
        elif(a[5][0][0]!="Y" and a[5][0][2]!="Y" and a[5][2][0]!="Y" and
           a[0][0][0]=="Y" and a[2][0][0]=="Y" and a[3][0][0]=="Y"):
            cb.move("LP")
            cb.move("UP")
            cb.move("L")
            cb.move("UP")
            cb.move("LP")
            cb.move("U2")
            cb.move("L")
            list2 += "LP UP L UP LP U2 L "
            a = cb.__repr__()
            
        # ORANGE   
        elif(a[5][0][0]!="Y" and a[5][2][0]!="Y" and a[5][2][2]!="Y" and
           a[0][0][0]=="Y" and a[1][0][0]=="Y" and a[3][0][0]=="Y"):
            cb.move("FP")
            cb.move("UP")
            cb.move("F")
            cb.move("FP")
            cb.move("FP")
            cb.move("U2")
            cb.move("F")
            list2 += "FP UP F UP FP U2 F "
            a = cb.__repr__()
            
        #BLUE
        elif(a[5][0][2]!="Y" and a[5][2][0]!="Y" and a[5][2][2]!="Y" and
           a[0][0][0]=="Y" and a[1][0][0]=="Y" and a[2][0][0]=="Y"):
            cb.move("RP")
            cb.move("UP")
            cb.move("R")
            cb.move("UP")
            cb.move("RP")
            cb.move("U2")
            cb.move("R")
            list2 += "RP UP R UP RP U2 R "
            a = cb.__repr__()
            
        #RED
        elif(a[5][0][0]!="Y" and a[5][0][2]!="Y" and a[5][2][2]!="Y" and
           a[1][0][0]=="Y" and a[2][0][0]=="Y" and a[3][0][0]=="Y"):
            cb.move("BP")
            cb.move("UP")
            cb.move("B")
            cb.move("UP")
            cb.move("BP")
            cb.move("U2")
            cb.move("B")
            list2 += "BP UP B UP BP U2 B "
            a = cb.__repr__()
        # TH3:
        #GREEN
        elif(a[5][0][0]=="Y" and a[5][0][1]=="Y" and a[5][0][2]=="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[0][0][0] == "Y" and a[0][0][2]=="Y"):
            cb.move("R2")
            cb.move("D")
            cb.move("RP")
            cb.move("U2")
            cb.move("R")
            cb.move("DP")
            cb.move("RP")
            cb.move("U2")
            cb.move("RP")
            list2 += "R2 D RP U2 R DP RP U2 RP "
            a = cb.__repr__()
        
        #ORANGE
        elif(a[5][0][0]=="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]=="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[1][0][0] == "Y" and a[1][0][2]=="Y"):
            cb.move("B2")
            cb.move("D")
            cb.move("BP")
            cb.move("U2")
            cb.move("B")
            cb.move("DP")
            cb.move("BP")
            cb.move("U2")
            cb.move("BP")
            list2 += "B2 D BP U2 B DP BP U2 BP "
            a = cb.__repr__()
        
        # BLUE
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]=="Y" and a[5][2][1]=="Y" and a[5][2][2]=="Y" and 
             a[2][0][0] == "Y" and a[2][0][2]=="Y"):
            cb.move("L2")
            cb.move("D")
            cb.move("LP")
            cb.move("U2")
            cb.move("L")
            cb.move("DP")
            cb.move("LP")
            cb.move("U2")
            cb.move("LP")
            list2 += "L2 D LP U2 L DP LP U2 LP "
            a = cb.__repr__()
        
        # RED
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]=="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]=="Y" and 
             a[3][0][0] == "Y" and a[3][0][2]=="Y"):
            cb.move("F2")
            cb.move("D")
            cb.move("FP")
            cb.move("U2")
            cb.move("F")
            cb.move("DP")
            cb.move("FP")
            cb.move("U2")
            cb.move("FP")
            list2 += "F2 D FP U2 F DP FP U2 FP "
            a = cb.__repr__()
        # TH4:
        #GREEN
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]=="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]=="Y" and 
             a[0][0][0] == "Y" and a[2][0][2]=="Y"):
            cb.move("L")
            cb.move("F")
            cb.move("RP")
            cb.move("FP")
            cb.move("LP")
            cb.move("F")
            cb.move("R")
            cb.move("FP")
            list2 += "L F RP FP LP F R FP "
            a = cb.__repr__()
        
        # ORANGE
        elif(a[5][0][0]=="Y" and a[5][0][1]=="Y" and a[5][0][2]=="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[1][0][0] == "Y" and a[3][0][2]=="Y"): #L-F; F-R; R-B
            cb.move("F")
            cb.move("R")
            cb.move("BP")
            cb.move("RP")
            cb.move("FP")
            cb.move("R")
            cb.move("B")
            cb.move("RP")
            list2 += "F R BP RP FP R B RP "
            a = cb.__repr__()
        
        # BLUE
        elif(a[5][0][0]=="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]=="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[0][0][2] == "Y" and a[2][0][0]=="Y"): #L-R; F-B; R-L
            cb.move("R")
            cb.move("B")
            cb.move("LP")
            cb.move("BP")
            cb.move("RP")
            cb.move("B")
            cb.move("L")
            cb.move("BP")
            list2 += "R B LP BP RP B L BP "
            a = cb.__repr__()
        
        # RED
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]=="Y" and a[5][2][1]=="Y" and a[5][2][2]=="Y" and 
             a[3][0][0] == "Y" and a[1][0][2]=="Y"): # L-B, F-L, R-F
            cb.move("B") 
            cb.move("L")
            cb.move("FP")
            cb.move("LP")
            cb.move("BP")
            cb.move("L")
            cb.move("F")
            cb.move("LP")
            list2 += "B L FP LP BP L F LP "
            a = cb.__repr__()
        # TH5: duong cheo
        #GREEN
        elif(a[5][0][0]=="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]=="Y" and 
             a[0][0][0] == "Y" and a[1][0][2]=="Y"):
            cb.move("RP")
            cb.move("F")
            cb.move("R")
            cb.move("BP")
            cb.move("RP")
            cb.move("FP")
            cb.move("R")
            cb.move("B")
            list2 += "RP F R BP RP FP R B "
            a = cb.__repr__()
        #ORANGE
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]=="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]=="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[1][0][0] == "Y" and a[2][0][2]=="Y"): # R-B; F:R; B:L
            cb.move("BP")
            cb.move("R")
            cb.move("B")
            cb.move("LP")
            cb.move("BP")
            cb.move("RP")
            cb.move("B")
            cb.move("L")
            list2 += "BP R B LP BP RP B L "
            a = cb.__repr__()
        #BLUE
        elif(a[5][0][0]=="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]=="Y" and 
             a[2][0][0] == "Y" and a[3][0][2]=="Y"): # R-L; F:B; B:F
            cb.move("LP")
            cb.move("B")
            cb.move("L")
            cb.move("FP")
            cb.move("LP")
            cb.move("BP")
            cb.move("L")
            cb.move("F")
            list2 += "LP B L FP LP BP L F "
            a = cb.__repr__()
        # RED
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]=="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]=="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[3][0][0] == "Y" and a[0][0][2]=="Y"): # R-F; F:L; B:R
            cb.move("FP")
            cb.move("L")
            cb.move("F")
            cb.move("RP")
            cb.move("FP")
            cb.move("LP")
            cb.move("F")
            cb.move("R")
            list2 += "FP L F RP FP LP F R "
            a = cb.__repr__()
        
        # TH6: Car
        #GREEN
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[1][0][0] == "Y" and a[1][0][2]=="Y" and 
             a[3][0][0] == "Y" and a[3][0][2]=="Y"): # (R U R' U) R U' R' U R U2 R'
            cb.move("R")
            cb.move("U")
            cb.move("RP")
            cb.move("U")
            cb.move("R")
            cb.move("UP")
            cb.move("RP")
            cb.move("U")
            cb.move("R")
            cb.move("U2")
            cb.move("RP")
            list2 += "R U RP U R UP RP U R U2 RP "
            a = cb.__repr__()
        #ORANGE, RED: R --> F
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[0][0][0] == "Y" and a[0][0][2]=="Y" and 
             a[2][0][0] == "Y" and a[2][0][2]=="Y"): # (R U R' U) R U' R' U R U2 R'
            cb.move("F")
            cb.move("U")
            cb.move("FP")
            cb.move("U")
            cb.move("F")
            cb.move("UP")
            cb.move("FP")
            cb.move("U")
            cb.move("F")
            cb.move("U2")
            cb.move("FP")
            list2 += "F U FP U F UP FP U F U2 FP "
            a = cb.__repr__()
        # TH7: Car 2
        #GREEN
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[0][0][2] == "Y" and a[2][0][0]=="Y" and 
             a[3][0][0] == "Y" and a[3][0][2]=="Y"): # R' U2 R2 U R2 U R2 U2 R'
            cb.move("RP")
            cb.move("U2")
            cb.move("R2")
            cb.move("U")
            cb.move("R2")
            cb.move("U")
            cb.move("R2")
            cb.move("U2")
            cb.move("RP")
            list2 += "RP U2 R2 U R2 U R2 U2 RP "
            a = cb.__repr__()
        #ORANGE
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[1][0][2] == "Y" and a[3][0][0]=="Y" and 
             a[0][0][0] == "Y" and a[0][0][2]=="Y"): # R-->B
            cb.move("BP")
            cb.move("U2")
            cb.move("B2")
            cb.move("U")
            cb.move("B2")
            cb.move("U")
            cb.move("B2")
            cb.move("U2")
            cb.move("BP")
            list2 += "BP U2 B2 U B2 U B2 U2 BP "
            a = cb.__repr__()
        # blue
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[2][0][2] == "Y" and a[0][0][0]=="Y" and 
             a[1][0][0] == "Y" and a[1][0][2]=="Y"): # R->L
            cb.move("LP")
            cb.move("U2")
            cb.move("L2")
            cb.move("U")
            cb.move("L2")
            cb.move("U")
            cb.move("L2")
            cb.move("U2")
            cb.move("LP")
            list2 += "LP U2 L2 U L2 U L2 U2 LP "
            a = cb.__repr__()
        # red
        elif(a[5][0][0]!="Y" and a[5][0][1]=="Y" and a[5][0][2]!="Y" and
             a[5][1][0]=="Y" and a[5][1][1]=="Y" and a[5][1][2]=="Y" and
             a[5][2][0]!="Y" and a[5][2][1]=="Y" and a[5][2][2]!="Y" and 
             a[3][0][2] == "Y" and a[1][0][0]=="Y" and 
             a[2][0][0] == "Y" and a[2][0][2]=="Y"): # R->F
            cb.move("FP")
            cb.move("U2")
            cb.move("F2")
            cb.move("U")
            cb.move("F2")
            cb.move("U")
            cb.move("F2")
            cb.move("U2")
            cb.move("FP")
            list2 += "FP U2 F2 U F2 U F2 U2 FP "
            a = cb.__repr__()
    
    return cb, list2

def OLL(cb):
    a = cb.__repr__()
    cb1, sol1 = cross_UP(cb)
    print(sol1)
    cb2, sol2 = full_UP(cb1)
    
    #print(cb2)
    sol = sol1 + sol2
    #print(sol)
    return cb, sol


            
        
