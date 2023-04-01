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
                terrain_heuristic(child)
                print(child.heuristic)
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




def uniform_cost_search(root : TreeNode, goal : TreeNode): # same as bfs since our cost is always 1
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






def manhattan_distance(curr_node : TreeNode, goal : TreeNode):
    
    
    
    if (len(curr_node.state.location) != len(goal.state.location)):
        location1 = curr_node.state.location[0]
        location2 = curr_node.state.location[1]
        y1 = location1[0]
        x1 = location1[1]
        y2 = location2[0]
        x2 = location2[1]

        y1 = round((y1 + y2) / 2)
        x1 = round((x1 + x2) / 2)

        location1 = goal.state.location[0]
        ygoal = location1[0]
        xgoal = location1[1]

        heuristic = abs(y1 - ygoal) + abs(x1 - xgoal)
        curr_node.set_heuristic(heuristic)



    else:
        location = curr_node.state.location[0]
        y = location[0]
        x = location[1]

        location = goal.state.location[0]
        ygoal = location[0]
        xgoal = location[1]

        heuristic = abs(y - ygoal) + abs(x - xgoal)
        curr_node.set_heuristic(heuristic)

    return None


def terrain_heuristic(curr_node : TreeNode):
    heuristic = 0
    
    visited = []
    for location in curr_node.state.location:
        top, bottom, left, right = False, False, False, False
        yL = location[0]
        xL = location[1]
        if yL > 0 :
           if  curr_node.state.statemap.loadedMap[yL - 1][xL].type == 0 and (yL - 1, xL) not in visited and [yL - 1, xL] not in curr_node.state.location:
                heuristic += 1
                top = True
                postion = [yL - 1, xL]
                visited.append(postion)
        if yL < curr_node.state.statemap.size[0] - 1:
            if curr_node.state.statemap.loadedMap[yL + 1][xL].type == 0 and (yL + 1, xL) not in visited and [yL + 1, xL] not in curr_node.state.location:
                heuristic += 1
                bottom = True
                postion = (yL + 1, xL)
                visited.append(postion)
        if xL > 0:
            if curr_node.state.statemap.loadedMap[yL][xL - 1].type == 0 and (yL, xL - 1) not in visited and [yL, xL - 1] not in curr_node.state.location:
                heuristic += 1
                left = True
                postion = (yL, xL - 1)
                visited.append(postion)
        if xL < curr_node.state.statemap.size[1] - 1:
            if curr_node.state.statemap.loadedMap[yL][xL + 1].type == 0 and (yL, xL + 1) not in visited and [yL, xL + 1] not in curr_node.state.location:
                heuristic += 1
                right = True
                postion = (yL, xL + 1)
                visited.append(postion)
        if top and left:
            if curr_node.state.statemap.loadedMap[yL - 1][xL - 1].type == 0:
                heuristic += 1
        if top and right:
            if curr_node.state.statemap.loadedMap[yL - 1][xL + 1].type == 0:
                heuristic += 1
        if bottom and left:
            if curr_node.state.statemap.loadedMap[yL + 1][xL - 1].type == 0:
                heuristic += 1
        if bottom and right:
            if curr_node.state.statemap.loadedMap[yL + 1][xL + 1].type == 0:
                heuristic += 1
    
    curr_node.set_heuristic(heuristic)
    return None


        





            

        
            







            

            
            
                

                    
            
                

            