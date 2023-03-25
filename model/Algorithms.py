from model.control import Control
from model.map import maps
from drawing.display import Display
from drawing.box import Box
from model.box import Box as cube
import pygame
import model.TreeNode as TreeNode

def bfs(node: TreeNode):
    queue = []
    queue.append(node)
    visited = []
    visited.append(node.state.currBoxLocation)
    while queue:
        node = queue.pop(0)
        if node.state.checkGoal():
            
            return node
        for move in node.state.moves:
            print(node.state)
            new_state = move()
            if new_state != False:
                child = TreeNode.TreeNode(new_state,node)
                if child.state.currBoxLocation not in visited:
                    print(node.state.currBoxLocation)
                    child.add_path(node.state.currBoxLocation)
                    visited.append(child.state.currBoxLocation)
                    node.addChild(child)
                    queue.append(child)
            
            

        
            







            

            
            
                

                    
            
                

            