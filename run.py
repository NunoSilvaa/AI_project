import pygame
import sys
from drawing.display import Display
from model.map import maps
from model.control import Control
import model.TreeNode as TreeNode
from model.Algorithms import *
from model.state import State
import time



class Level:
    lv1  = "./level/1.json"
    lv2 = "./level/2.json"
    lv3 = "./level/3.json"
    lv4 = "./level/4.json"
    lv5 = "./level/5.json"
    lv6 = "./level/6.json"
    lv7 = "./level/7.json"
    lv8 = "./level/8.json"
    lv9 = "./level/9.json"
    lv10 = "./level/10.json"
    lv11 = "./level/11.json"
    lv12 = "./level/12.json"
    lv13 = "./level/13.json"
    lv14 = "./level/14.json"
    lv15 = "./level/15.json"
    lv16 = "./level/16.json"

def draw_path_3D(solution, timesleep=0.5, level=Level.lv1, map_size = (0,0),display = None):
    
    
    
    
    if solution != None:
        print("Success!")
        
        choiselv = maps(level)


        choiselv.drawMaps()
        choiselv.currBox.drawBox()
        
        display.update() 

        for path in solution:
            choiselv.currBox.location = path

            '''for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return'''
            
            
            
            choiselv.currBox.drawBox()
            choiselv.drawMaps()
            display.update()
            pygame.time.delay(420)
            
            
        pygame.quit()
        return

    else:
        print("Unable to find path for maps!")
        print("Dir Level: %s" % level)
        return






    
def main(level=Level.lv1, Play=True,Algorithm=None,Heuristic=None):
    print("Processing...")
    Maps = maps(level)
    size = Maps.size
    control = Control(Maps)
    pygame.init()
    display = Display(title='Bloxorz Game', map_size=(size[0], size[1]))
    result = True
    
    
    print("Press space Key to Exit!")
    while True:
        # os.system("clear")
        if Play:
            
            
            for event in pygame.event.get():
                if Play:
                    if event.type == pygame.KEYUP and event.key == ord('w'):
                        result = control.moveUp()
                    elif event.type == pygame.KEYDOWN and event.key == ord('s'):
                        result = control.moveDown()
                    elif event.type == pygame.KEYDOWN and event.key == ord('d'):
                        result = control.moveRight()
                    elif event.type == pygame.KEYDOWN and event.key == ord('a'):
                        result = control.moveLeft()
                    
                if display.quit(event):
                    return
            Maps.drawMaps()
            Maps.currBox.drawBox()
            display.update()

            if control.checkGoal():
                print("WINNER!")
                return
            if result == False:
                print("LOSER!")
                return
        else:
            root = TreeNode.TreeNode(State(Maps.currBox.location,Maps))
            goal = TreeNode.TreeNode(State([Maps.end],Maps))

            if Algorithm is None:
                print("An algorithm must be selected!")
                return
            else:
                start = time.time()
                end = 0
                if Algorithm == "BFS":
                    solution = bfs(root, goal)
                    end = time.time()
                    if solution != None:
                        path = solution.get_path()
                        draw_path_3D(path, level=level, map_size=(size[0], size[1]),display=display)
                    
                elif Algorithm == "DFS":
                    solution = dfs(root, goal)
                    end = time.time()
                    if solution != None:
                        path = solution.get_path()
                        draw_path_3D(path, level=level, map_size=(size[0], size[1]),display=display)
                    
                elif Algorithm == "IDDFS":
                    solution = iddfs(root, goal,100 )
                    end = time.time()
                    if solution != None:
                        path = solution.get_path()
                        draw_path_3D(path, level=level, map_size=(size[0], size[1]),display=display)
                
                elif Algorithm == "GREADY":
                    solution = greedy_search(root, goal, Heuristic)
                    end = time.time()
                    if solution != None:
                        path = solution.get_path()
                        draw_path_3D(path, level=level, map_size=(size[0], size[1]),display=display)
                elif Algorithm == "UC":
                    solution = uniform_cost_search(root,goal)
                    end = time.time()
                    if solution != None:
                        path = solution.get_path()
                        draw_path_3D(path, level=level, map_size=(size[0], size[1]),display=display)
                elif Algorithm == "A*":
                        solution = a_star(root,goal, Heuristic)
                        end = time.time()
                        if solution != None:
                            path = solution.get_path()
                            draw_path_3D(path, level=level, map_size=(size[0], size[1]),display=display)
                    
                print(Algorithm + " took " + str(end - start) + " seconds to complete.")
                print("Completed in " + str(len(solution.get_path())) + " moves.")
                return

if __name__=="__main__":
    if len(sys.argv) > 2:
        level = sys.argv[1]
        option = sys.argv[2]
        if option != "play":
            print("Error! Please read file README.md for more details. thanks")
            sys.exit()
            
        if option == "play": 
            main(level=level, Play=True)

        else: 
            print("Error! Please read file README.md for more details. thanks")
    else:
        # Edit here
        main(level=Level.lv2, Play=False, Algorithm="A*", Heuristic="manhattan")