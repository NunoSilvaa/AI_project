from model.state import State

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.heuristic = -1
        
        
        if parent != None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def create_children(self):
        up = self.state.moveUp()
        down = self.state.moveDown()
        left = self.state.moveLeft()
        right = self.state.moveRight()
        if up != None:
            self.add_child(TreeNode(up, self))
        if down != None:
            self.add_child(TreeNode(down,self))
        if left != None:
            self.add_child(TreeNode(left,self))
        if right != None:
            self.add_child(TreeNode(right,self))

    def get_path(self):
        path = []
        node = self
        while node != None:
            path.insert(0, node.state.location)
            node = node.parent
        return path
    

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

        