from model.map import maps
import copy
class State:
    
    def __init__(self, location, statemap):
        self.location = location
        self.statemap = statemap

    def __eq__(self, other):
        if other == None:
            return False
        if len(self.location) != len(other.location):
            return False
        if len(self.location) > 1:
            return self.location[0] == other.location[0] and self.location[1] == other.location[1]
        elif len(self.location) == 1:
            return self.location[0] == other.location[0]
        
        
    def moveUp(self):
        self.statemap.currBox.moveUp()
        if self.statemap.onFloor():
            
            newLocation = self.statemap.currBox.location.copy()
            newStatemap = copy.deepcopy(self.statemap)
            self.statemap.currBox.moveDown()
            return State(newLocation, newStatemap)
        else:
            self.statemap.currBox.moveDown()
            return None
    
    def moveDown(self):
        self.statemap.currBox.moveDown()
        if self.statemap.onFloor():
                newLocation = self.statemap.currBox.location.copy()
                newStatemap = copy.deepcopy(self.statemap)
                self.statemap.currBox.moveUp()
                return State(newLocation, newStatemap)

        else:
            self.statemap.currBox.moveUp()
            return None
        
    def moveRight(self):
        self.statemap.currBox.moveRight()
        if self.statemap.onFloor():
                
                newLocation = self.statemap.currBox.location.copy()
                newStatemap = copy.deepcopy(self.statemap)
                self.statemap.currBox.moveLeft()
                return State(newLocation, newStatemap)
        else:
            self.statemap.currBox.moveLeft()
            return None
    
    def moveLeft(self):
        self.statemap.currBox.moveLeft()
        if self.statemap.onFloor():
            
            newLocation = self.statemap.currBox.location.copy()
            newStatemap = copy.deepcopy(self.statemap)
            self.statemap.currBox.moveRight()
            return State(newLocation, newStatemap)
        else:
            self.statemap.currBox.moveRight()
            return None
    



        

        
            
            
    

    