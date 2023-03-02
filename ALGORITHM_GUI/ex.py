from cube import Cube
from cross import SOLVE_CROSS
from f2l import FLOOR_2ND
from oll import OLL
from pll import PLL
from T import T
    
str = [[["G", "B", "W"], ["R", "G", "Y"], ["B", "W", "O"]],
       [["B", "B", "R"], ["G", "O", "R"], ["Y", "B", "W"]],
       [["G", "O", "O"], ["Y", "B", "R"], ["G", "W", "R"]],
       [["Y", "W", "W"], ["G", "R", "W"], ["B", "G", "W"]],
       [["R", "O", "B"], ["O", "W", "Y"], ["Y", "B", "O"]],
       [["G", "Y", "Y"], ["G", "Y", "O"], ["R", "R", "O"]]]


#str = "OYBYGOWGOYWYWOGBGRBBGOBGYBOROWWRBGBRBYWRWRYOGWWRYYRGRO"

 
cb = Cube(str)
a = cb.__repr__()
    

def SOLVE(cb):
    print("Initial State: \n")
    print(cb)
    
    cb1, sol1 = SOLVE_CROSS(cb)
    print(cb1)
    cb2, sol2 = T(cb1)
    print(cb2)
    cb3, sol3 = FLOOR_2ND(cb2)
    print(cb3)
    cb4, sol4 = OLL(cb3)
    print(cb4)
    cb5, sol5 = PLL(cb4)
    
    print("Cross: ", sol1)
    print("\n")
    print("T: ", sol2)
    print("\n")
    print("2ndFloor: ", sol3)
    print("\n")
    print("Oll: ", sol4)
    print("\n")
    print("Pll: ", sol5)
    print("\n")
    print("Solved Rubik! \n")
    print(cb5)
    
    sol = sol1+sol2+sol3+sol4+sol5
    return cb, sol

SOLVE(cb)
    
