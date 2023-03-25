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


    def moveUp(self):  
        self.levelMap.currBox.moveUp()
        return self.checkBoxOnMaps()
    
    def moveDown(self):
        
        self.levelMap.currBox.moveDown()
        return self.checkBoxOnMaps()
    
    def moveRight(self):
        
        self.levelMap.currBox.moveRight()
        return self.checkBoxOnMaps()

    
    def moveLeft(self):
        
        self.levelMap.currBox.moveLeft()
        return self.checkBoxOnMaps()

    
        
        
        

    def checkBoxOnMaps(self):
        return self.levelMap.onFloor()

    
    def checkGoal(self):
        return self.levelMap.checkGoal()
    
    
    

    
    '''def drawStartBox(self):
        if len(self.boxStartLocation) == 2:
            currLocation = self.boxStartLocation
        else: 
            currLocation = [self.boxStartLocation[0], self.boxStartLocation[0]]
        
            BoxStart = Box("#", len(self.boxStartLocation), self.boxStartLocation)

            if BoxStart.isStanding():
                Cube.drawBox(position=(currLocation[0][1], currLocation[0][0]), size=(1, 1, 2), border_color=(0.8, 0.8, 0.8))
            elif BoxStart.isVertical():
                Cube.drawBox(position=(currLocation[1][1], currLocation[1][0]), size=(1, 2, 1), border_color=(0.8, 0.8, 0.8))
            elif BoxStart.isHorizontal():
                Cube.drawBox(position=(currLocation[0][1], currLocation[0][0]), size=(2, 1, 1), border_color=(0.8, 0.8, 0.8))'''
    
    '''def drawStartMaps(self):
        height, width = self.size
        startMap = self.startMap
        for x in range(width):
            for y in range(height):
                tile = startMap[int(y)][int(x)]
                if tile.type != 0:
                    Cube.drawBox(position=(x, y), size=(1, 1, -0.3), face_color=tile.colors)'''