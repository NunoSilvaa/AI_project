import simplejson as json
from model.box import Box
from drawing.box import Box as Cube
from model.tiles import tile
class goal:
    def __init__(self, symbol, location):
        self.symbol = symbol
        self.location = location
        
class maps:
    def __init__(self, path=None):
        
        self.jsonObj = None
        self.loadedMap = list()
        self.level = None
        self.size = None
        self.start = None
        self.end = None 
        self.currBox = None
        self.tileTypes = None
        if path != None:
            self.loadLevel(path)

    def loadLevel(self, path=None):
        if path != None:
            files = open(path, "r")
            self.jsonObj = json.loads(files.read())

            # Name Level
            self.level = self.jsonObj["level"]
            # Size Map
            self.size = self.jsonObj["size"]
            # Start Location
            self.start = self.jsonObj["start"]
            # End Location
            self.end = self.jsonObj["end"]
            # Types of tiles
            self.tileTypes = [self.jsonObj["tiles"]["floor"], self.jsonObj["tiles"]["void"], self.jsonObj["tiles"]["edge"], self.jsonObj["tiles"]["teleport"]] 
            # Current Box
            boxObj = self.jsonObj["box"]
            self.currBox = Box(boxObj["symbol"], boxObj["location"])

            #Teleports
            self.teleports = [self.jsonObj["teleports"]["tp1"], self.jsonObj["teleports"]["tp2"]]

            # Load Maps
            self.__loadMap()

        else: print("Path_to_level not None")
        
    
    def __loadMap(self):
        # Load tiles to Maps
        loadedMap = self.jsonObj["maps"]
        for i in range(self.size[0]):
            line = []
            for j in range(self.size[1]):
                if loadedMap[i][j] == self.tileTypes[0]: # rock tile
                    newtile = tile(1, None, [i, j])
                    line.append(newtile)
                elif loadedMap[i][j] == self.tileTypes[2]: # edge tile
                    newtile = tile(2, None, [i, j])
                    line.append(newtile)
                
                elif loadedMap[i][j] == self.tileTypes[3]:
                    if self.teleports[0] == [i, j]:
                        newtile = tile(3,None, [i, j], self.teleports[1])
                    else:
                        newtile = tile(3,None, [i, j], self.teleports[0])
                    

                    line.append(newtile)
                
                elif loadedMap[i][j] == self.tileTypes[1]: # space title
                    newtile = tile(0, None, [i, j])
                    if self.end == [i, j]:
                        newtile.setObj(goal("$", [i, j])) # End game
                    line.append(newtile)
                else:
                    newtile = tile(1, None, [i, j])
                    line.append(newtile)
            self.loadedMap.append(line)
    

    
    def __isGoal(self):
        return self.end == self.currBox.location[0]

    def checkGoal(self):
        return self.currBox.isStanding()  and self.__isGoal()

    def __isValid(self, box):
        if len(box.location) == 1:
            x , y = box.location[0]
            return self.loadedMap[x][y].checkTile(box)
        elif len(box.location) == 2:
            for child in box.location:
                x, y = child
                if not self.loadedMap[x][y].checkTile(box): 
                    return False
            return True
    
    def onFloor(self):
        width, height = self.size
        if len(self.currBox.location) == 1:
            y, x = self.currBox.location[0]
            if y < 0 or y >= width or x < 0 or x >= height:
                return False
            return self.__isValid(self.currBox)
        elif len(self.currBox.location) == 2:
            for child in self.currBox.location:
                y , x = child
                if y < 0 or y >= width or x < 0 or x >= height:
                    return False
            return self.__isValid(self.currBox)
        

    def drawMaps(self, path=None):
        height, width = self.size
        levelMap = self.loadedMap
        for x in range(width):
            for y in range(height):
                tile = levelMap[int(y)][int(x)]
                if tile.type != 0:
                    
                    Cube.drawBox(position=(x, y), size=(1, 1, -0.3), face_color=tile.colors)
                else:
                    if tile.obj != None and tile.obj.symbol == "$":
                        Cube.drawBox(position=(x, y), size=(1, 1, -0.3), face_color=tile.colors)






    
