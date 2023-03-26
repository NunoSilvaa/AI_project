class State:
    
    def __init__(self, location, direction):
        self.location = location
        self.direction = direction

    def __eq__(self, other):
        if len(self.location) > 1:
            return self.location[0] == other.location[0] and self.location[1] == other.location[1] and self.direction == other.direction
        else:
            return self.location[0] == other.location[0] and self.direction == other.direction
        
    def moveUp(self):
        if self.direction == 1:
            
    

    