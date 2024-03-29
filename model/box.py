from drawing.box import Box as Cube


class Direction:
    standing = 1
    horizontal = 2
    vertical = 3

"""Box"""
class Box:
    def __init__(self, symbol, location):
        self.symbol = symbol
        self.active = False
        self.location = location
        


    def moveUp(self):
        numGPS = len(self.location)
        if numGPS == 1:
            yi, xi = self.location[0]
            newYi1, newYi2  = int(yi-1), int(yi-2)
            newLocation = [[newYi1, xi],[newYi2, xi]]
            self.changeLocation(newLocation)
        else:
            if self.isHorizontal():
                y1, x1 = self.location[0]
                y2, x2 = self.location[1]
                newY1, newY2 = int(y1-1), int(y2-1)
                newLocation = [[newY2, x1], [newY1, x2]]
                self.changeLocation(newLocation)
            elif self.isVertical():
                yi, xi = self.location[1]
                newYi = int(yi-1)
                newLocation = [[newYi, xi]]
                self.changeLocation(newLocation)

    def moveRight(self):
        numGPS = len(self.location)
        if numGPS == 1:
            yi, xi = self.location[0]
            newXi1, newXi2 = int(xi+1), int(xi+2)
            newLocation = [[yi, newXi1],[yi, newXi2]]
            self.changeLocation(newLocation)
        else:
            if self.isHorizontal():
                yi, xi = self.location[1]
                newXi = int(xi+1)
                newLocation = [[yi, newXi]]
                self.changeLocation(newLocation)
            elif self.isVertical():
                y1, x1 = self.location[0]
                y2, x2 = self.location[1]
                newX1, newX2 = int(x1+1), int(x2+1)
                newLocation = [[y1, newX1],[y2, newX2]]
                self.changeLocation(newLocation)

    def moveLeft(self):
        numGPS = len(self.location)
        if numGPS == 1:
            yi, xi = self.location[0]
            newXi1, newXi2 = int(xi-1), int(xi-2)
            newLocation = [[yi, newXi2],[yi, newXi1]]
            self.changeLocation(newLocation)
        else:
            if self.isHorizontal():
                yi, xi = self.location[0]
                newXi = int(xi-1)
                newLocation = [[yi, newXi]]
                self.changeLocation(newLocation)
            elif self.isVertical():
                y1, x1 = self.location[0]
                y2, x2 = self.location[1]
                newX1, newX2 = int(x1-1), int(x2-1)
                newLocation = [[y1, newX1],[y2, newX2]]
                self.changeLocation(newLocation)

    def moveDown(self):
        numGPS = len(self.location)
        if numGPS == 1:
            yi, xi = self.location[0]
            newYi1, newYi2 = int(yi+1), int(yi+2)
            newLocation = [[newYi2, xi],[newYi1, xi]]
            self.changeLocation(newLocation)
        else:
            if self.isHorizontal():
                y1, x1 = self.location[0]
                y2, x2 = self.location[1]
                newY1, newY2 = int(y1+1), int(y2+1)
                newLocation = [[newY1, x1], [newY2, x2]]
                self.changeLocation(newLocation)
            elif self.isVertical():
                yi, xi = self.location[0]
                newYi = int(yi+1)
                newLocation = [[newYi, xi]]
                self.changeLocation(newLocation)
        
    
    def getLocation(self):
        return self.location
    
    def checkDirection(self, location=None):
        if location != None:
            if len(location) == 2:
                y1, x1 = location[0]
                y2, x2 = location[1]
                if y1 == y2:
                    return Direction.horizontal
                if x1 == x2: 
                    return Direction.vertical
            else: return Direction.standing
        else:
            if len(self.location) == 2:
                y1, x1 = self.location[0]
                y2, x2 = self.location[1]
                if y1 == y2:
                    return Direction.horizontal
                if x1 == x2: 
                    return Direction.vertical
            else: return Direction.standing
            
    def changeLocation(self, location):
        self.location = location

    def on(self):
        self.active = True

    def off(self):
        self.active = False
    
    def isHorizontal(self):
        return self.checkDirection() == Direction.horizontal
    
    def isVertical(self):
        return self.checkDirection() == Direction.vertical
    
    def isStanding(self):
        return len(self.location) == Direction.standing
    
    def drawBox(self):
        if len(self.location) == 2:
            currLocation = self.location
        else: currLocation = [self.location[0], self.location[0]]

        if self.isStanding():
            Cube.drawBox(position=(currLocation[0][1], currLocation[0][0]), size=(1, 1, 2), border_color=(0.8, 0.8, 0.8))
        elif self.isVertical():
            Cube.drawBox(position=(currLocation[1][1], currLocation[1][0]), size=(1, 2, 1), border_color=(0.8, 0.8, 0.8))
        elif self.isHorizontal():
            Cube.drawBox(position=(currLocation[0][1], currLocation[0][0]), size=(2, 1, 1), border_color=(0.8, 0.8, 0.8))
            
