import simplejson as json
from model.box import Box
from model.tiles import tile
class goal:
    def __init__(self, symbol, location):
        self.symbol = symbol
        self.location = location
        
class maps:
    def __init__(self, path_to_level=None):
        self.files = None
        self.jsonObj = None
        self.maps = list()
        self.level = None
        self.size = None
        self.start = None
        self.end = None 
        self.current_box = None
        self.types_tile = None
        if path_to_level != None:
            self.loadLevel(path_to_level)

    def loadLevel(self, path_to_level=None):
        if path_to_level != None:
            self.files = open(path_to_level, "r")
            self.jsonObj = json.loads(self.files.read())

            # Name Level
            self.level = self.jsonObj["level"]
            # Size Map
            self.size = self.jsonObj["size"]
            # Start Location
            self.start = self.jsonObj["start"]
            # End Location
            self.end = self.jsonObj["end"]
            # Types of tiles
            self.types_tile = [self.jsonObj["tiles"]["floor"], self.jsonObj["tiles"]["void"]]
            # Current Box
            boxObj = self.jsonObj["box"]
            self.current_box = Box(boxObj["symbol"], boxObj["location"])

            # Load Maps
            self.__loadMap()

        else: print("Path_to_level not None")
    
    def __loadMap(self):
        # Load tiles to Maps
        maps = self.jsonObj["maps"]
        for i in range(self.size[0]):
            line = []
            for j in range(self.size[1]):
                if maps[i][j] == self.types_tile[0]: # rock tile
                    newtile = tile(1, None, [i, j])
                    line.append(newtile)
                elif maps[i][j] == self.types_tile[1]: # space title
                    newtile = tile(0, None, [i, j])
                    if self.end == [i, j]:
                        newtile.setObj(goal("$", [i, j])) # End game
                    line.append(newtile)
                else:
                    newtile = tile(1, None, [i, j])
                    line.append(newtile)
            self.maps.append(line)
    
    def refreshBox(self):
        if not self.__onFloor(self.current_box):
            self.current_box.location = self.current_box.pre_location
            return False
        return True

    
    def __isGoal(self):
        return self.end == self.current_box.location[0]

    def checkGoal(self):
        return self.current_box.isStanding()  and self.__isGoal()
     
    def __isValid(self, box):
        if len(box.location) == 1:
            y , x = box.location[0]
            return self.maps[y][x].checkTile(box)
        elif len(box.location) == 2:
            for child in box.location:
                y, x = child
                if not self.maps[y][x].checkTile(box): 
                    return False
            return True
    
    def __onFloor(self, box):
        width, height = self.size
        if len(box.location) == 1:
            y, x = box.location[0]
            if y < 0 or y >= width or x < 0 or x >= height:
                return False
            return self.__isValid(box)
        elif len(box.location) == 2:
            for child in box.location:
                y , x = child
                if y < 0 or y >= width or x < 0 or x >= height:
                    return False
            return self.__isValid(box)


    def printCurrent(self):
        for i in self.maps:
            print("------" * self.size[1])
            print('{0: <3}'.format("|"), end='')
            for j in i:
                if j.type == 0:
                    content = " "
                    if j.obj != None:
                        if j.obj.symbol == "$":
                            content = "$"
                elif j.type == 1 or j.type == 2:
                    if j.obj != None:
                        content = j.obj.symbol
                    else: content = j.type
                if j.location in self.current_box.location:
                    content = "#"
                print('{0: <2}'.format(content),"|", end='')
                print('{0: <2}'.format(""), end='')
            print("\n",end='')
        print("------" * self.size[1])

    
