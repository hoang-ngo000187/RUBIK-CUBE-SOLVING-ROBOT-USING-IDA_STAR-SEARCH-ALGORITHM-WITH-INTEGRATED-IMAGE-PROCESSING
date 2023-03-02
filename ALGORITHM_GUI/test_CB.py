from cube import Cube
from cross import SOLVE_CROSS
from f2l import FLOOR_2ND
from T import T
from oll import OLL
from pll import PLL
from __init1__ import solve
# BFDLUDRLLDBFDRRDRFBUBUFFLDRBLFBDFFUURBDRLBRRULLUUBDLFU
"""
str = [[["G", "O", "O"], ["W", "G", "Y"], ["B", "W", "R"]],
       [["Y", "R", "W"], ["O", "O", "R"], ["Y", "B", "W"]],
       [["B", "G", "R"], ["Y", "B", "W"], ["G", "O", "O"]],
       [["Y", "B", "W"], ["R", "R", "G"], ["Y", "G", "W"]],
       [["R", "O", "G"], ["Y", "W", "Y"], ["B", "B", "O"]],
       [["B", "R", "O"], ["W", "Y", "B"], ["R", "G", "G"]]]

str = [[["O", "R", "Y"], ["W", "G", "O"], ["Y", "Y", "W"]],
       [["G", "Y", "R"], ["W", "O", "Y"], ["O", "G", "G"]],
       [["B", "B", "R"], ["B", "B", "R"], ["R", "B", "Y"]],
       [["W", "W", "W"], ["Y", "R", "B"], ["B", "O", "B"]],
       [["R", "O", "B"], ["G", "W", "W"], ["O", "R", "Y"]],
       [["G", "O", "W"], ["R", "Y", "G"], ["G", "G", "O"]]]

str = [[["B", "Y", "W"], ["O", "G", "Y"], ["Y", "O", "R"]],
       [["B", "W", "G"], ["R", "O", "B"], ["W", "Y", "R"]],
       [["W", "R", "G"], ["Y", "B", "G"], ["B", "B", "G"]],
       [["O", "G", "O"], ["W", "R", "B"], ["W", "R", "R"]],
       [["G", "W", "B"], ["G", "W", "O"], ["R", "W", "Y"]],
       [["Y", "B", "O"], ["O", "Y", "R"], ["Y", "G", "O"]]]
"""

def str_state(string):
    
    string = string.replace("F", "G")
    string = string.replace("R", "O")
    string = string.replace("B", "B")
    string = string.replace("L", "R")
    string = string.replace("D", "W")
    string = string.replace("U", "Y")
        
    
    x = [
        [[], [], []],
        [[], [], []],
        [[], [], []],
        [[], [], []],
        [[], [], []],
        [[], [], []]
        ]
    
    x[0][0] = list(string[18:21])
    x[0][1] = list(string[21:24])
    x[0][2] = list(string[24:27])
    
    x[1][0] = list(string[9:12])
    x[1][1] = list(string[12:15])
    x[1][2] = list(string[15:18])
    
    x[2][0] = list(string[45:48])
    x[2][1] = list(string[48:51])
    x[2][2] = list(string[51:])
    
    x[3][0] = list(string[36:39])
    x[3][1] = list(string[39:42])
    x[3][2] = list(string[42:45])
    
    x[4][0] = list(string[27:30])
    x[4][1] = list(string[30:33])
    x[4][2] = list(string[33:36])
    
    x[5][0] = list(string[:3])
    x[5][1] = list(string[3:6])
    x[5][2] = list(string[6:9])
    return x
    
    
def replace(string):
    # XP = X'
    string = string.replace("UP ", "U' ")
    string = string.replace("RP ", "R' ")
    string = string.replace("FP ", "F' ")
    string = string.replace("DP ", "D' ")
    string = string.replace("LP ", "L' ")
    string = string.replace("BP ", "B' ")
    # X X = X2
    string = string.replace("U U ", "U2 ")
    string = string.replace("R R ", "R2 ")
    string = string.replace("F F ", "F2 ")
    string = string.replace("D D ", "D2 ")
    string = string.replace("L L ", "L2 ")
    string = string.replace("B B ", "B2 ")
    # X X2 = X'
    string = string.replace("U U2 ", "U' ")
    string = string.replace("R R2 ", "R' ")
    string = string.replace("F F2 ", "F' ")
    string = string.replace("D D2 ", "D' ")
    string = string.replace("L L2 ", "L' ")
    string = string.replace("B B2 ", "B' ")
    # X2 X = X'
    string = string.replace("U2 U ", "U' ")
    string = string.replace("R2 R ", "R' ")
    string = string.replace("F2 F ", "F' ")
    string = string.replace("D2 D ", "D' ")
    string = string.replace("L2 L ", "L' ")
    string = string.replace("B2 B ", "B' ")
    # X X' = ""
    string = string.replace("U U' ", " ")
    string = string.replace("R R' ", " ")
    string = string.replace("F F' ", " ")
    string = string.replace("D D' ", " ")
    string = string.replace("L L' ", " ")
    string = string.replace("B B' ", " ")
    # X' X = ""
    string = string.replace("U' U ", " ")
    string = string.replace("R' R ", " ")
    string = string.replace("F' F ", " ")
    string = string.replace("D' D ", " ")
    string = string.replace("L' L ", " ")
    string = string.replace("B' B ", " ")
    # X2 X' = X
    string = string.replace("U2 U' ", "U ")
    string = string.replace("R2 R' ", "R ")
    string = string.replace("F2 F' ", "F ")
    string = string.replace("D2 D' ", "D ")
    string = string.replace("L2 L' ", "L ")
    string = string.replace("B2 B' ", "B ")
    # X' X2 = X
    string = string.replace("U' U2 ", "U ")
    string = string.replace("R' R2 ", "R ")
    string = string.replace("F' F2 ", "F ")
    string = string.replace("D' D2 ", "D ")
    string = string.replace("L' L2 ", "L ")
    string = string.replace("B' B2 ", "B ")
    
    # X' X' = X2
    string = string.replace("U' U' ", "U2 ")
    string = string.replace("R' R' ", "R2 ")
    string = string.replace("F' F' ", "F2 ")
    string = string.replace("D' D' ", "D2 ")
    string = string.replace("L' L' ", "L2 ")
    string = string.replace("B' B' ", "B2 ")
    return string
    
    
def solve_CB(string):
    state = str_state(string)
    
    cb = Cube(state)
    a = cb.__repr__()
    
    cb1, sol1 = SOLVE_CROSS(cb)
    print("CROSS: ",sol1)
    print(cb1)
    
    cb2, sol2 = T(cb1)
    print("T: ", sol2)
    print(cb2)
    
    cb3, sol3 = FLOOR_2ND(cb2)
    print("FLOOR_2ND: ", sol3)
    print(cb3)
    
    cb4, sol4 = OLL(cb3)
    print("OLL: ", sol4)
    print(cb4)
    
    cb5, sol5 = PLL(cb4)
    print("PLL: ", sol5)
    
    solve = sol1+sol2+sol3+sol4+sol5
    solve = replace(solve)
    #list_solve = solve.split(" ")
    #len_solve = len(list_solve)
    
    #print("SOLVE:\r\n", solve)
    #print("Length: ", len(list_solve))
    print(cb5)
    return solve
# U R F D L B
str = [[["B", "Y", "W"], ["O", "G", "Y"], ["Y", "O", "R"]], # F
       [["B", "W", "G"], ["R", "O", "B"], ["W", "Y", "R"]], # R
       [["W", "R", "G"], ["Y", "B", "G"], ["B", "B", "G"]], # B
       [["O", "G", "O"], ["W", "R", "B"], ["W", "R", "R"]], # L
       [["G", "W", "B"], ["G", "W", "O"], ["R", "W", "Y"]], # D
       [["Y", "B", "O"], ["O", "Y", "R"], ["Y", "G", "O"]]] # U

#S = "RDRFUURFDLBFBRRUUUFLFLFRLDLDBFBDFRFBURUULUDLBDLBDBRLDB"
S = "FBBLUDLFRDFRFRURLBUUFRFLBLBLUUDDBLDLUDFFLUDBDDRRBBRURF"
print(str_state(S))
solve = solve_CB(S)

print(solve)

