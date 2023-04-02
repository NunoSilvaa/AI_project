import sys
from drawing.box import Box as Cube
from model.map import maps as levelMap
from model.tiles import tile as Tile

class Control:
    
    def __init__(self, levelMap: levelMap):
        if levelMap is None:
            print("Maps not None")
            sys.exit()
        
        # MAP
        self.levelMap = levelMap


    def __check_teleport(self,tyle):
        if tyle.type == 3:
            return True
        return False

    def moveUp(self):
        
        

        self.levelMap.currBox.moveUp()
        tyle = self.levelMap.loadedMap[self.levelMap.currBox.location[0][0]][self.levelMap.currBox.location[0][1]]
        if self.__check_teleport(tyle):
            self.levelMap.currBox.location = [tyle.tpLocation]
        return self.levelMap.onFloor()
    
    def moveDown(self):
        
        self.levelMap.currBox.moveDown()
        tyle = self.levelMap.loadedMap[self.levelMap.currBox.location[0][0]][self.levelMap.currBox.location[0][1]]
        if self.__check_teleport(tyle):
            self.levelMap.currBox.location = [tyle.tpLocation]
        return self.levelMap.onFloor()
    
    def moveRight(self):
        
        self.levelMap.currBox.moveRight()
        tyle = self.levelMap.loadedMap[self.levelMap.currBox.location[0][0]][self.levelMap.currBox.location[0][1]]
        if self.__check_teleport(tyle):
            self.levelMap.currBox.location = [tyle.tpLocation]
        return self.levelMap.onFloor()

    
    def moveLeft(self):
        
        self.levelMap.currBox.moveLeft()
        tyle = self.levelMap.loadedMap[self.levelMap.currBox.location[0][0]][self.levelMap.currBox.location[0][1]]
        if self.__check_teleport(tyle):
            self.levelMap.currBox.location = [tyle.tpLocation]
        return self.levelMap.onFloor()

    

    
    def checkGoal(self):
        return self.levelMap.checkGoal()
    
    
    

    
   