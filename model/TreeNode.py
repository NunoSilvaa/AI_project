# A generic definition of a tree node holding a state of the problem
from model.control import Control
class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.path = []

    
    def addChild(self, child):
        self.children.append(child)

    def add_path(self,new_path):
        self.path.append(new_path)
    
    def get_path(self):
        return self.path

    '''def __eq__(self, other):
        print(other.state)
        return self.state.currBoxLocation == other.state.currBoxLocation'''





        