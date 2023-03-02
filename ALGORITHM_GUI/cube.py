class Cube:
    
    def __init__(self, faces = "None"):
        self.orientation = [[5, 1, 4, 3], [5, 2, 4, 0], [5, 3, 4, 1], [5, 0, 4, 2], [0, 1, 2, 3], [2, 1, 0, 3]]
        self.rotmap = [[[2, 0], [2, 1], [2, 2], [0, 0], [1, 0], [2, 0], [0, 2], [0, 1], [0, 0], [2, 2], [1, 2], [0, 2]], [[2, 2], [1, 2], [0, 2], [0, 0], [1, 0], [2, 0], [2, 2], [1, 2], [0, 2], [2, 2], [1, 2], [0, 2]], [[0, 2], [0, 1], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [1, 2], [0, 2]], [[0, 0], [1, 0], [2, 0], [0, 0], [1, 0], [2, 0], [0, 0], [1, 0], [2, 0], [2, 2], [1, 2], [0, 2]], [[2, 0], [2, 1], [2, 2], [2, 0], [2, 1], [2, 2], [2, 0], [2, 1], [2, 2], [2, 0], [2, 1], [2, 2]], [[0, 2], [0, 1], [0, 0], [0, 2], [0, 1], [0, 0], [0, 2], [0, 1], [0, 0], [0, 2], [0, 1], [0, 0]]]
        self.sideTocmap = ["G", "O", "B", "R", "W", "Y"]
        self.faces = faces
        if(faces == "None"):
            self.cube = [[[self.sideTocmap[c]] * 3 for _ in range(3)] for c in range(6)]
        else:
            self.cube = faces
    
    def __repr__(self):
        return self.faces
    
    def __str__(self):
        pstr = ""
        for i in range(3):
            pstr += "    "
            for j in range(3):
                pstr += self.cube[5][i][j]
            pstr += "\n"
        for i in range(3):
            for j in range(3):
                pstr += self.cube[3][i][j]
            pstr += " "
            for j in range(3):
                pstr += self.cube[0][i][j]
            pstr += " "
            for j in range(3):
                pstr += self.cube[1][i][j]
            pstr += " "
            for j in range(3):
                pstr += self.cube[2][i][j]
            pstr += "\n"
        for i in range(3):
            pstr += "    "
            for j in range(3):
                pstr += self.cube[4][i][j]
            if(i != 2):
                pstr += "\n"
        return pstr

    def rotateClock(self, side):
        temp = [self.cube[side][0][1], self.cube[side][0][2]]
        self.cube[side][0][1] = self.cube[side][1][0]
        self.cube[side][0][2] = self.cube[side][0][0]
        self.cube[side][0][0] = self.cube[side][2][0]
        self.cube[side][1][0] = self.cube[side][2][1]
        self.cube[side][2][0] = self.cube[side][2][2]
        self.cube[side][2][1] = self.cube[side][1][2]
        self.cube[side][1][2] = temp[0]
        self.cube[side][2][2] = temp[1]
        temp = [self.cube[self.orientation[side][0]][self.rotmap[side][0][0]][self.rotmap[side][0][1]], self.cube[self.orientation[side][0]][self.rotmap[side][1][0]][self.rotmap[side][1][1]], self.cube[self.orientation[side][0]][self.rotmap[side][2][0]][self.rotmap[side][2][1]]]
        for i in range(3):
            self.cube[self.orientation[side][0]][self.rotmap[side][0 + i][0]][self.rotmap[side][0 + i][1]] = self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]]
            self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]] = self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]]
            self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]] = self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]]
            self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]] = temp[0 + i]

    def rotateAntiClock(self, side):
        temp = [self.cube[side][0][1], self.cube[side][0][2]]
        self.cube[side][0][1] = self.cube[side][1][2]
        self.cube[side][0][2] = self.cube[side][2][2]
        self.cube[side][1][2] = self.cube[side][2][1]
        self.cube[side][2][2] = self.cube[side][2][0]
        self.cube[side][2][0] = self.cube[side][0][0]
        self.cube[side][2][1] = self.cube[side][1][0]
        self.cube[side][0][0] = temp[1]
        self.cube[side][1][0] = temp[0]
        temp = [self.cube[self.orientation[side][0]][self.rotmap[side][0][0]][self.rotmap[side][0][1]], self.cube[self.orientation[side][0]][self.rotmap[side][1][0]][self.rotmap[side][1][1]], self.cube[self.orientation[side][0]][self.rotmap[side][2][0]][self.rotmap[side][2][1]]]
        for i in range(3):
            self.cube[self.orientation[side][0]][self.rotmap[side][0 + i][0]][self.rotmap[side][0 + i][1]] = self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]]
            self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]] = self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]]
            self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]] = self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]]
            self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]] = temp[0 + i]

    def rotateMidClock(self, type):
        if(type == 'E'):
            temp = [self.cube[0][1][0], self.cube[0][1][1], self.cube[0][1][2]]
            for i in range(3):
                self.cube[0][1][0 + i] = self.cube[3][1][0 + i]
                self.cube[3][1][0 + i] = self.cube[2][1][0 + i]
                self.cube[2][1][0 + i] = self.cube[1][1][0 + i]
                self.cube[1][1][0 + i] = temp[0 + i]
        elif(type == 'M'):
            temp = [self.cube[0][0][1], self.cube[0][1][1], self.cube[0][2][1]]
            for i in range(3):
                self.cube[0][0 + i][1] = self.cube[5][0 + i][1]
                self.cube[5][0 + i][1] = self.cube[2][2 - i][1]
                self.cube[2][2 - i][1] = self.cube[4][0 + i][1]
                self.cube[4][0 + i][1] = temp[0 + i]
        elif(type == 'S'):
            temp = [self.cube[5][1][0], self.cube[5][1][1], self.cube[5][1][2]]
            for i in range(3):
                self.cube[5][1][0 + i] = self.cube[3][2 - i][1]
                self.cube[3][2 - i][1] = self.cube[4][1][2 - i]
                self.cube[4][1][2 - i] = self.cube[1][0 + i][1]
                self.cube[1][0 + i][1] = temp[0 + i]

    def rotateMidAntiClock(self, type):
        if(type == 'E'):
            temp = [self.cube[0][1][0], self.cube[0][1][1], self.cube[0][1][2]]
            for i in range(3):
                self.cube[0][1][0 + i] = self.cube[1][1][0 + i]
                self.cube[1][1][0 + i] = self.cube[2][1][0 + i]
                self.cube[2][1][0 + i] = self.cube[3][1][0 + i]
                self.cube[3][1][0 + i] = temp[0 + i]
        elif(type == 'M'):
            temp = [self.cube[0][0][1], self.cube[0][1][1], self.cube[0][2][1]]
            for i in range(3):
                self.cube[0][0 + i][1] = self.cube[4][0 + i][1]
                self.cube[4][0 + i][1] = self.cube[2][2 - i][1]
                self.cube[2][2 - i][1] = self.cube[5][0 + i][1]
                self.cube[5][0 + i][1] = temp[0 + i]
        elif(type == 'S'):
            temp = [self.cube[5][1][0], self.cube[5][1][1], self.cube[5][1][2]]
            for i in range(3):
                self.cube[5][1][0 + i] = self.cube[1][0 + i][1]
                self.cube[1][0 + i][1] = self.cube[4][1][2 - i]
                self.cube[4][1][2 - i] = self.cube[3][2 - i][1]
                self.cube[3][2 - i][1] = temp[0 + i]
    
    def move(self, type):
        if(type == 'U'):
            self.rotateClock(5)
            #print("U")
        elif(type == 'UP'):
            self.rotateAntiClock(5)
            #print("UP")
        elif(type == 'U2'):
            self.rotateClock(5)
            self.rotateClock(5)
            #print("U2")
        elif(type == 'D'):
            self.rotateClock(4)
            #print("D")
        elif(type == 'DP'):
            self.rotateAntiClock(4)
            #print("DP")
        elif(type == 'D2'):
            self.rotateClock(4)
            self.rotateClock(4)
            #print("D2")
        elif(type == 'R'):
            self.rotateClock(1)
            #print("R")
        elif(type == 'RP'):
            self.rotateAntiClock(1)
            #print("RP")
        elif(type == 'R2'):
            self.rotateClock(1)
            self.rotateClock(1)
            #print("R2")
        elif(type == 'L'):
            self.rotateClock(3)
            #print("L")
        elif(type == 'LP'):
            self.rotateAntiClock(3)
            #print("LP")
        elif(type == 'L2'):
            self.rotateClock(3)
            self.rotateClock(3)
            #print("L2")
        elif(type == 'F'):
            self.rotateClock(0)
            #print("F")
        elif(type == 'FP'):
            self.rotateAntiClock(0)
            #print("FP")
        elif(type == 'F2'):
            self.rotateClock(0)
            self.rotateClock(0)
            #print("F2")
        elif(type == 'B'):
            self.rotateClock(2)
            #print("B")
        elif(type == 'BP'):
            self.rotateAntiClock(2)
            #print("BP")
        elif(type == 'B2'):
            self.rotateClock(2)
            self.rotateClock(2)
            #print("B2")
"""
str = [[["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]],
       [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
       [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]],
       [["R", "R", "R"], ["R", "R", "R"], ["R", "R", "R"]],
       [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]],
       [["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]]]
"""
                



    