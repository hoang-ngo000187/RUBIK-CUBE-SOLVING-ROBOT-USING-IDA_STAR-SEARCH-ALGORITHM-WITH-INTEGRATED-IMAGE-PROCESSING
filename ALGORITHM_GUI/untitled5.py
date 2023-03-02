#from __init1__ import solve

"""
 U: WHITE
 R: BLUE
 F: RED
 B: ORANGE
 L: GREEN
 D: YELLOW
"""

# U - R - F - D - L - B
#cube_str = "DRRBUFFFBDUBDRDRRBRRRBFLUDUFFFFDBDLLBDDULLFLLUULRBBUUL"
#cube_str = "FBUDUDDRDFFBLRFLURRURBFDRBFUUUUDFBFUDBBDLLDLBLRLRBRFLL"
#print(solve(cube_str))

a = "H*e*llo*"
b = "e"

c = a.find("*", 0, len(a))

if c!=0:
    print("False")
else:
    print("True")
