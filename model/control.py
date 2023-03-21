import sys
from drawing.box import Box as Cube
from model.box import Box 
from copy import deepcopy
from model.map import maps as levelMap
from model.tiles import tile as Tile
import math
import numpy as np

class Control:
    Play = False
    def __init__(self, levelMap: levelMap):
        if levelMap is None:
            print("Maps not None")
            sys.exit()
        
        # BOX
        self.boxStartLocation = levelMap.currBox.location
        self.currBoxLocation = levelMap.currBox.location
        
        # MAP
        self.levelMap = levelMap
        self.startMap = self.levelMap.loadedMap[:]
        self.currMap = self.startMap
        self.size = levelMap.size


    def moveUp(self):
        self.levelMap.currBox.moveUp()
        if not self.checkBoxOnMaps():
            return False
        else:
            self.updateLocation()
            return True 
    
    def moveDown(self):
        self.levelMap.currBox.moveDown()
        if not self.checkBoxOnMaps():
            return False
        else:
            self.updateLocation() 
            return True 
    
    def moveRight(self):
        self.levelMap.currBox.moveRight()
        if not self.checkBoxOnMaps():
            return False
        else:
            self.updateLocation()
            return True 
    
    def moveLeft(self):
        self.levelMap.currBox.moveLeft()
        if not self.checkBoxOnMaps():
            return False
        else:
            self.updateLocation()
            return True

    def updateLocation(self):
        self.currBoxLocation = self.levelMap.currBox.location
        self.currMap == self.levelMap.loadedMap
        

    def checkBoxOnMaps(self):
        return self.levelMap.refreshBox()

    
    def checkGoal(self):
        return self.levelMap.checkGoal()
    
    
    def drawMaps(self, path=None):
        height, width = self.size
        levelMap = self.currMap
        for x in range(width):
            for y in range(height):
                tile = levelMap[int(y)][int(x)]
                if tile.type != 0:
                    # if [y, x] in self.current or [y, x] in path:
                    #     Cube.drawBox(position=(x, y), size=(1, 1, -0.3), face_color=Tile.mark)
                    Cube.drawBox(position=(x, y), size=(1, 1, -0.3), face_color=tile.colors)
                else:
                    if tile.obj != None and tile.obj.symbol == "$":
                        Cube.drawBox(position=(x, y), size=(1, 1, -0.3), face_color=tile.colors)

    def drawBox(self):
        if len(self.currBoxLocation) == 2:
            currLocation = self.currBoxLocation
        else: currLocation = [self.currBoxLocation[0], self.currBoxLocation[0]]

        if self.levelMap.currBox.isStanding():
            Cube.drawBox(position=(currLocation[0][1], currLocation[0][0]), size=(1, 1, 2), border_color=(0.8, 0.8, 0.8))
        elif self.levelMap.currBox.isVertical():
            Cube.drawBox(position=(currLocation[1][1], currLocation[1][0]), size=(1, 2, 1), border_color=(0.8, 0.8, 0.8))
        elif self.levelMap.currBox.isHorizontal():
            Cube.drawBox(position=(currLocation[0][1], currLocation[0][0]), size=(2, 1, 1), border_color=(0.8, 0.8, 0.8))
    
    def drawStartBox(self):
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
                Cube.drawBox(position=(currLocation[0][1], currLocation[0][0]), size=(2, 1, 1), border_color=(0.8, 0.8, 0.8))
    
    def drawStartMaps(self):
        height, width = self.size
        startMap = self.startMap
        for x in range(width):
            for y in range(height):
                tile = startMap[int(y)][int(x)]
                if tile.type != 0:
                    Cube.drawBox(position=(x, y), size=(1, 1, -0.3), face_color=tile.colors)