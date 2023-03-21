colors = {
		'gray'	:(	 0.56862745, 0.56862745, 0.56862745, 1),
        'orange':(   0.96470588, 0.34509804, 0.05882352, 1), 
        'green' :(   0.50196078, 0.91372549, 0.09019607, 1),
        'white' :(   0.8       ,        0.8,        0.8, 1),
        'yellow' :( 1.0, 0.792156862745098, 0.0941176470588235, 0.3),
        'mark' : (0.9058823529411765, 1.0, 0.4431372549019608, 0.5)
	}

class tile:
    
    mark = colors['mark']
    FLOOR = 1
    VOID = 0
    
    def __init__(self, typ, obj, location):
        self.type = typ
        self.obj = obj
        self.location = location
        self.colors = colors['white']
        self.setColor()
        
        
    def setColor(self):

        if self.type == 1:
            self.colors = colors['gray']


        if self.obj != None:
            if '$' in str(self.obj.symbol):
                self.colors = colors['yellow']
             
    def checkTile(self, box):
        for child in box.location:
            if child == self.location:
                # void
                if self.type == tile.VOID:
                    if self.obj != None:
                        if self.obj.symbol == "$":
                            return True
                        else: return False
                    else: return False
                # floor
                elif self.type == tile.FLOOR: 
                    return True
        return False

    def getLocation(self):
        return self.location
    
    def setObj(self, obj):
        self.obj = obj
        self.setColor()