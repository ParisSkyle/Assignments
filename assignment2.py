class Mapp():
    def __init__(self,size): self.size, self.map = size, [[0] * size for i in  range(size)]
    def PrintMap(self):
        plus_sign = "+"  * (self.size + 2)
        print(plus_sign)
        for i in self.map:
            print("+", end = "")
            for j in i:
                if j == 0: print(" ", end = "")
                else: print("*", end = "")
            print("+")
        print(plus_sign)
    def Update(self,column,line): self.map[column][line] = 1
class Vehicle():
    def __init__(self,column = 0,line = 0,brush_position = "up",directon = "right"):
        self.column, self.line, self.brush_position,self.direction, self.directions = column, line, brush_position, directon, ["right", "down", "left", "up"]
    def Turn(self,times = 1,where = "right"):
        if where == "right":
            for i in range(times):
                try: self.direction = self.directions[self.directions.index(self.direction) + 1]
                except: self.direction = self.directions[0]
        elif where == "left":
            for i in range(times):
                try: self.direction = self.directions[self.directions.index(self.direction) - 1]
                except: self.direction = self.directions[3]
    def Move(self,count,map):
        if self.brush_position == "down": map.Update(column = self.column, line = self.line)  
        if count > map.size: count = (count % map.size) + map.size      
        for i in range(count):
            if self.direction == "right":
                if 1 + self.line < map.size: self.line += 1
                else: self.line = 0
                if self.brush_position == "down": map.Update(column = self.column, line = self.line)
            elif self.direction == "left":
                if self.line - 1 < 0: self.line = self.line + map.size - 1
                else: self.line -= 1
                if self.brush_position == "down": map.Update(column = self.column, line = self.line)
            elif self.direction == "up": 
                if self.column - 1 < 0: self.column = self.column + map.size - 1
                else: self.column -= 1
                if self.brush_position == "down": map.Update(column = self.column, line = self.line)
            else:
                if self.column + 1 < map.size: self.column += 1
                else: self.column = 0
                if self.brush_position == "down": map.Update(column = self.column, line = self.line)
    def Jump(self,map):
        if self.brush_position == "down": 
            map.Update(column = self.column, line = self.line)
            self.brush_position = "up"
        self.Move(count = 3,map = map)
def GUI():
    instruction_list = ["<-----RULES----->","1. BRUSH DOWN","2. BRUSH UP","3.VEHICLE ROTATES RIGHT","4. VEHICLE ROTATES LEFT","5. MOVE UP TO X","6. JUMP","7. REVERSE DIRECTION","8. VIEW THE MATRIX","0. EXIT","Please enter the commands with a plus sign (+) between them."]
    for i in instruction_list: print(i)
def Warning(): print("You entered an incorrect command. Please try again!")
def main():
    try:
        inpts, toy_car = input().split("+"), Vehicle()
        try: 
            if inpts[-1] != "0": Warning(), main()
        except: Warning(), main()
        mp = Mapp(size = int(inpts[0])) 
        inpts.pop(0)
    except: Warning(), main() 
    for i in inpts:
        try:       
            if i == "1": 
                toy_car.brush_position = "down"
                mp.Update(column= toy_car.column, line= toy_car.line)
            elif i == "2": toy_car.brush_position = "up"
            elif i == "3": toy_car.Turn()
            elif i == "4": toy_car.Turn(where = "left")
            elif i.startswith("5_"): toy_car.Move(map = mp, count = int(i[2:]))                
            elif i == "6": toy_car.Jump(map = mp)
            elif i == "7": toy_car.Turn(times = 2)
            elif i == "8": mp.PrintMap()
            elif i == "0": quit
            else: Warning(), main()
        except: Warning(), main()  
GUI()
main()