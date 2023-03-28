import model.TreeNode as TreeNode

def bfs(root: TreeNode, goal: TreeNode):
    queue = []
    queue.append(root)
    visited = [root.state]

    while queue:
        curr_node = queue.pop(0)
        
        if curr_node.state == goal.state:
            return curr_node
        curr_node.create_children()
        for child in curr_node.children:
            if child.state not in visited:
                visited.append(child.state)
                queue.append(child)
    return None


def dfs(root: TreeNode, goal: TreeNode):
    stack = []
    stack.append(root)
    visited = [root.state]

    while stack:
        curr_node = stack.pop()
        
        if curr_node.state == goal.state:
            return curr_node
        curr_node.create_children()
        for child in curr_node.children:
            if child.state not in visited:
                visited.append(child.state)
                stack.append(child)
    return None


def dls(root: TreeNode, goal: TreeNode, max_depth: int):
    stack = []
    stack.append(root)
    visited = [root.state]

    while stack:
        curr_node = stack.pop()
        if curr_node.state == goal.state:
            return curr_node
        if curr_node.depth < max_depth:
            curr_node.create_children()
            for child in curr_node.children:
                if child.state not in visited:
                    visited.append(child.state)
                    stack.append(child)
    return None

def iddfs(root: TreeNode, goal: TreeNode, max_depth: int):
    for i in range(max_depth):
        result = dls(root, goal, i)
        if result != None:
            return result
    return None




def uniform_cost_search(root : TreeNode, goal : TreeNode):
    stack = []
    stack.append(root)
    visited = [root.state]

    while stack:
        curr_node = stack.pop(0)
        if curr_node.state == goal.state:
            return curr_node
        curr_node.create_children()
        for child in curr_node.children:
            if child.state not in visited:
                visited.append(child.state)
                stack.append(child)
        stack = sorted(stack,key = lambda x : x.depth , reverse = False  )
    return None


            
            

        
            







            

            
            
                

                    
            
                

            