from cube import Cube

"""
Front: G --> R index = 0
Right: O --> B index = 1
Back: B --> O index = 2
Left: R --> G index = 3
Down: W --> Y index = 4
Up: Y --> W index = 5
"""

str = [[["G", "B", "W"], ["R", "G", "Y"], ["B", "W", "O"]],
       [["B", "B", "R"], ["G", "O", "R"], ["Y", "B", "W"]],
       [["G", "O", "O"], ["Y", "B", "R"], ["G", "W", "R"]],
       [["Y", "W", "W"], ["G", "R", "W"], ["B", "G", "W"]],
       [["R", "O", "B"], ["O", "W", "Y"], ["Y", "B", "O"]],
       [["G", "Y", "Y"], ["G", "Y", "O"], ["R", "R", "O"]]]

cb = Cube(str)
a = cb.__repr__()

def check_edgeW_1(cb):
    a=cb.__repr__()
    cross_solve1 = ""
    #GREEN
    if(a[5][2][1]=="W"):
        print("")
        cross_solve1 += " "
    elif(a[1][1][0]=="W"):
        cb.move('FP')
        cross_solve1 += "FP "
        a=cb.__repr__()
    elif(a[4][0][1]=="W"):
        cb.move('F2')
        cross_solve1 += "F2 "
        a=cb.__repr__()
    elif(a[3][1][2]=="W"):
        cb.move('F')
        cross_solve1 += "F "
        a=cb.__repr__()
    
        # ORANGE
    if(a[5][1][2]=="W"):
        print("")
        cross_solve1 += " "
    elif(a[2][1][0]=="W"):
        cb.move('RP')
        cross_solve1 += "RP "
        a=cb.__repr__()
    elif(a[4][1][2]=="W"):
        cb.move('R2')
        cross_solve1 += "R2 "
        a=cb.__repr__()
    elif(a[0][1][2]=="W"):
        cb.move('R')
        cross_solve1 += "R "
        a=cb.__repr__()
    
    #BLUE
    if(a[5][0][1]=="W"):
        print(" ")
    elif(a[3][1][0]=="W"):
        cb.move('BP')
        cross_solve1 += "BP "
        a=cb.__repr__()
    elif(a[4][2][1]=="W"):
        cb.move('B2')
        cross_solve1 += "B2 "
        a=cb.__repr__()
    elif(a[1][1][2]=="W"):
        cb.move('B')
        cross_solve1 += "B "
        a=cb.__repr__()
            
            #RED
    if(a[5][1][0]=="W"):
        print("")
    elif(a[0][1][0]=="W"):
        cb.move('LP')
        cross_solve1 += "LP "
        a=cb.__repr__()
    elif(a[4][1][0]=="W"):
        cb.move('L2')
        cross_solve1 += "L2 "
        a=cb.__repr__()
    elif(a[2][1][2]=="W"):
        cb.move('L')
        cross_solve1 += "L "
        a=cb.__repr__()
        
    return cb, cross_solve1  

def check_edgeW_2(cb): # Kiem tra X2 co bằng W khong?
    cross_solve2 = ""
    a=cb.__repr__()
    while True:
        if(a[0][0][1]=="W"):
            cb.move('F')
            cb.move('UP')
            cb.move('R')
            cross_solve2 += "F UP R "
            a=cb.__repr__()
        if(a[1][0][1]=="W"):
            cb.move('R')
            cb.move('UP')
            cb.move('B')
            cross_solve2 += "R UP B "
            a=cb.__repr__()
        if(a[2][0][1]=="W"):
            cb.move('B')
            cb.move('UP')
            cb.move('L')
            cross_solve2 += "B UP L "
            a=cb.__repr__()
        if(a[3][0][1]=="W"):
            cb.move('L')
            cb.move('UP')
            cb.move('F')
            cross_solve2 += "L UP F "
            a=cb.__repr__()
        if(a[0][0][1]!="W" and a[1][0][1]!="W" and a[2][0][1]!="W" and a[3][0][1]!="W"):
            break
    return cb, cross_solve2

def check_edgeW_3(cb): # 
    cross_solve3 = ""
    a = cb.__repr__()
    
    while True:
        if(a[0][1][0]!="W" and a[0][1][2]!="W" and
           a[1][1][0]!="W" and a[1][1][2]!="W" and
           a[2][1][0]!="W" and a[2][1][2]!="W" and
           a[3][1][0]!="W" and a[3][1][2]!="W"):
            break
        
        if(a[0][1][0]=="W"):
            while True:
                if(a[5][1][0]!="W"):
                    cb.move('LP')
                    cross_solve3 += "LP "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
                
        if(a[0][1][2]=="W"):
            while True:
                if(a[5][1][0]!="W"):
                    cb.move('R')
                    cross_solve3 += "R "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
        #Orange
        if(a[1][1][0]=="W"):
            while True:
                if(a[5][2][1]!="W"):
                    cb.move('FP')
                    cross_solve3 += "FP "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
                
        if(a[1][1][2]=="W"):
            while True:
                if(a[5][0][1]!="W"):
                    cb.move('B')
                    cross_solve3 += "B "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
        # Blue
        if(a[2][1][0]=="W"):
            while True:
                if(a[5][1][2]!="W"):
                    cb.move('RP')
                    cross_solve3 += "RP "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
                
        if(a[2][1][2]=="W"):
            while True:
                if(a[5][1][0]!="W"):
                    cb.move('L')
                    cross_solve3 += "L "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
        # Red
        if(a[3][1][0]=="W"):
            while True:
                if(a[5][0][1]!="W"):
                    cb.move('BP')
                    cross_solve3 += "BP "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
                
        if(a[3][1][2]=="W"):
            while True:
                if(a[5][2][1]!="W"):
                    cb.move('F')
                    cross_solve3 += "F "
                    a=cb.__repr__()
                    break
                cb.move('U')
                cross_solve3 += "U "
                a=cb.__repr__()
                
    return cb, cross_solve3

def check_edgeW_5(cb):
    cross_solve5 = ""
    a = cb.__repr__()
    if (a[4][0][1]=="W"):
        while True:
            if(a[5][2][1]!="W"):
                cb.move('F2')
                cross_solve5 += "F2 "
                a=cb.__repr__()
                break
            cb.move('U')
            cross_solve5 += "U "
            a=cb.__repr__()
    
    if (a[4][1][2]=="W"):
        while True:
            if(a[5][1][2]!="W"):
                cb.move('R2')
                cross_solve5 += "R2 "
                a=cb.__repr__()
                break
            cb.move('U')
            cross_solve5 += "U "
            a=cb.__repr__()
            
    if (a[4][2][1]=="W"):
        while True:
            if(a[5][0][1]!="W"):
                cb.move('B2')
                cross_solve5 += "B2 "
                a=cb.__repr__()
                break
            cb.move('U')
            cross_solve5 += "U "
            a=cb.__repr__()
    
    if (a[4][1][0]=="W"):
        while True:
            if(a[5][1][0]!="W"):
                cb.move('L2')
                cross_solve5 += "L2 "
                a=cb.__repr__()
                break
            cb.move('U')
            cross_solve5 += "U "
            a=cb.__repr__()
    return cb, cross_solve5

def check_edgeW_6(cb): # con vien trang o mat duoi
    a = cb.__repr__()
    cross_solve6 = ""
    # Green
    if(a[0][2][1]=="W"):
        while True:
            if(a[5][2][1]!="W"):
                cb.move("F2")
                cb.move('F')
                cb.move('UP')
                cb.move('R')
                cross_solve6 += "F2 F UP R "
                a=cb.__repr__()
                break
            cb.move("U")
            cross_solve6 += "U "
        
        
    
    #Orange
    if(a[1][2][1]=="W"):
        while True:
            if(a[5][1][2]!="W"):
                cb.move("R2")
                cb.move('R')
                cb.move('UP')
                cb.move('B')
                cross_solve6 += "R2 R UP B "
                a=cb.__repr__()
                break
            cb.move("U")
            cross_solve6 += "U "
        
        
    
    # Blue
    if(a[2][2][1]=="W"):
        while True:
            if(a[5][0][1]!="W"):
                cb.move("B2")
                cb.move('B')
                cb.move('UP')
                cb.move('L')
                cross_solve6 += "B2 B UP L "
                a=cb.__repr__()
                break
            cb.move("U")
            cross_solve6 += "U "
        
        
        
    # Red
    if(a[3][2][1]=="W"):
        while True:
            if(a[5][1][0]!="W"):
                cb.move("L2")
                cb.move('L')
                cb.move('UP')
                cb.move('F')
                cross_solve6 += "L2 L UP F "
                a=cb.__repr__()
                break
            cb.move("U")
            cross_solve6 += "U "

    return cb, cross_solve6
    
def check_edgeW_4(cb):
    a = cb.__repr__()
    cross_solve4 = ""
    while True:
        if(a[0][0][1]=="G" and a[5][2][1]=="W"):
            cb.move('F2')
            cross_solve4 += "F2 "
            a=cb.__repr__()
            break
        cb.move('U')
        cross_solve4 += "U "
        a=cb.__repr__()
    while True:
        if(a[1][0][1]=="O" and a[5][1][2]=="W"):
            cb.move('R2')
            cross_solve4 += "R2 "
            a=cb.__repr__()
            break
        cb.move('U')
        cross_solve4 += "U "
 
        a=cb.__repr__()
    while True:
        if(a[2][0][1]=="B" and a[5][0][1]=="W"):
            cb.move('B2')
            cross_solve4 += "B2 "
            a=cb.__repr__()
            break
        cb.move('U')
        cross_solve4 += "U "
        a=cb.__repr__()
    while True:
        if(a[3][0][1]=="R" and a[5][1][0]=="W"):
            cb.move('L2')
            cross_solve4 += "L2 "
            a=cb.__repr__()
            break
        cb.move('U')
        cross_solve4 += "U "
        a=cb.__repr__()
    return cb, cross_solve4

def SOLVE_CROSS(cb):
    solve_replace = ""
    cb1, solve1 = check_edgeW_1(cb)
    cb2, solve2 = check_edgeW_2(cb1)
    cb3, solve3 = check_edgeW_3(cb2)
    cb5, solve5 = check_edgeW_5(cb3)
    cb6, solve6 = check_edgeW_6(cb5)
    cb4, solve4 = check_edgeW_4(cb6)
    solve = solve1 + solve2 + solve3 + solve5 + solve6 + solve4
    solve_replace=solve.replace("U U U ", "UP ")
    solve_replace=solve_replace.replace("U U ", "U2 ")
    return cb4, solve_replace

