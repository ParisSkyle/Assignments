import sys
class Mapper():
    def GetMap(self):
     with open(sys.argv[1]) as data: return [x.split(" ") for x in data.read().splitlines()]  
    def ShowMap(self):
        print()
        for x in self.map:
            for y in x: print(y,end=" ")
            print()
        print()
class Game(Mapper):
    def __init__(self):self.map,self.colors,self.score,self.playable = self.GetMap(),{"B": 9,"G": 8,"W": 7,"Y": 6,"R" :5,"P": 4,"O": 3,"D": 2,"F": 1,"X": 0," ": 0}, 0,True
    def immediateFinder(self,picked_cell_y,picked_cell_x):
        immidiate_location_list = []
        try:
            if self.map[picked_cell_y][picked_cell_x] != "X":
                try:
                    if self.map[picked_cell_y][picked_cell_x] == " ": print("\nPlease enter a valid size!\n")
                    else:
                        self.map[picked_cell_y][picked_cell_x]
                        immidiate_location_list = [[picked_cell_y,picked_cell_x]]
                        for location in immidiate_location_list:
                            try:
                                if self.map[location[0] + 1][location[1]] == self.map[location[0]][location[1]]:
                                    if [location[0] + 1,location[1]] not in immidiate_location_list: immidiate_location_list.append([location[0] + 1,location[1]])
                            except: pass
                            try:
                                if self.map[location[0] - 1][location[1]] == self.map[location[0]][location[1]] and location[0] - 1 != -1:
                                    if [location[0] - 1,location[1]] not in immidiate_location_list: immidiate_location_list.append([location[0] - 1,location[1]])
                            except: pass
                            try:
                                if self.map[location[0]][location[1] + 1] == self.map[location[0]][location[1]]:
                                    if [location[0],location[1] + 1] not in immidiate_location_list: immidiate_location_list.append([location[0],location[1] + 1])
                            except: pass
                            try:
                                if self.map[location[0]][location[1] - 1] == self.map[location[0]][location[1]] and location[1] - 1 != -1:
                                    if [location[0],location[1] - 1] not in immidiate_location_list: immidiate_location_list.append([location[0],location[1] - 1])
                            except: pass
                        if len(immidiate_location_list) > 1:
                            for location in immidiate_location_list:
                                self.score += self.colors[self.map[location[0]][location[1]]]
                                self.map[location[0]][location[1]] = " "
                            self.BlankFiller()
                            self.ShowMap()
                            print(f"Your score is: {candy_Crush.score}\n")
                        else: self.ShowMap()                         
                except: 
                    print("\nPlease enter a valid size!\n")
                    self.ShowMap()
            else:
                self.Bomb(x_picked= picked_cell_x,y_picked = picked_cell_y)
                self.BlankFiller()
                self.ShowMap()
                print(f"Your score is: {self.score}\n")
        except: print("\nPlease enter a valid size!\n")
    def BlankFiller(self):
        for c in range(len(self.map)):
            for y in self.map:
                i = 0
                if self.map.index(y) != len(self.map) - 1:
                    for x in y:
                        if self.map[self.map.index(y) + 1][y.index(x,i)] == " ":
                            self.map[self.map.index(y) + 1][y.index(x,i)] = x
                            self.map[self.map.index(y)][y.index(x,i)] = " "
                        i += 1
        for y in self.map:
            if y.count(" ") == len(self.map[0]): self.map.remove(y)
        x = 0
        while x < len(self.map[0]):
            if self.map[-1][x] == " ":
                for row in self.map:row.pop(x)
            else: x += 1
    def Is_Playable(self):
        self.playable = False
        for y in self.map:
            for x in y:
                if x != "X":
                    if x != " ":
                        try:
                            if x == self.map[self.map.index(y)][y.index(x) + 1]:
                                self.playable = True
                        except: pass
                        try:
                            if y.index(x) - 1 >= 0:
                                if x == self.map[self.map.index(y)][y.index(x) - 1]:
                                    self.playable = True
                        except: pass
                        try:
                            if x == self.map[self.map.index(y) + 1][y.index(x)]:
                                self.playable = True
                        except: pass
                        try:
                            if self.map.index(y) - 1 >= 0:
                                if x == self.map[self.map.index(y) - 1][y.index(x)]:
                                    self.playable = True
                        except: pass
                else: self.playable = True
    def Bomb(self,y_picked,x_picked):
        bomb_location_list = [[y_picked,x_picked]]
        for location in bomb_location_list:
            q = -1
            for y in self.map:
                if self.map.index(y) == location[0]:
                    for x in y:
                        q += 1
                        if y.index(x,q) == location[1]:
                            temp = y.index(x,q)
                            for c in range(len(self.map)):
                                if self.map[c][temp] == "X" and [c,temp] not in bomb_location_list: bomb_location_list.append([c,temp])                                    
                                self.score += self.colors[self.map[c][temp]]                           
                                self.map[c][temp] = " "
                            for z in range(len(y)):
                                if y[z] == "X" and [self.map.index(y),z] not in bomb_location_list: bomb_location_list.append([self.map.index(y),z])
                                self.score += self.colors[y[z]]
                                y[z] = " "
candy_Crush = Game() 
candy_Crush.ShowMap()
print(f"Your score is: {candy_Crush.score}\n")
while candy_Crush.playable:
    try:
        command = input("Please enter a row and column number: ").split(" ")
        candy_Crush.immediateFinder(int(command[0]), int(command[1]))
    except: print("\nWrong İnput ! Format will be like: int int\n") 
    candy_Crush.Is_Playable()
    if not candy_Crush.playable: print("Game Over!") 