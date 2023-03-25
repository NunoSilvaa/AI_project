import pygame
import sys
import os
import time
from drawing.display import Display
from model.map import maps
from model.control import Control
import model.TreeNode as TreeNode
from model.Algorithms import bfs


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


def draw_path_3D(solution, timesleep=0.5, level=Level.lv1, map_size = (0,0)):
    pygame.init()
    display = Display(title='Bloxorz Game', map_size=map_size)
    if solution != None:
        print("Success!")
        print("Step: %d" % len(solution))
        print(solution)
        choiselv = maps(level)

        level = Control(choiselv)
        level.draw_box()
        level.draw_maps()
        display.update() 

        for path in solution:
            time.sleep(timesleep)
            level.current = path
            level.update_box_locaton_for_maps(path)
            
            if level.maps.refreshBox():
                level.update_current_location()
            else: 
                print("Solution Fail!")
                return

            level.draw_box() 
            level.draw_maps()   
            display.update()
        return
    else:
        print("Unable to find path for maps!")
        print("Dir Level: %s" % level)
        return
    
    
def main(level=Level.lv1, Play=True,Algorithm=None):
    print("Processing...")
    Maps = maps(level)
    size = Maps.size
    state = Control(Maps)

    state.Play = Play
    pygame.init()
    display = Display(title='Bloxorz Game', map_size=(size[0], size[1]))
    result = True
    print("Press space Key to Exit!")
    while True:
        # os.system("clear")
        if Play:
            
            for event in pygame.event.get():
                if state.Play:
                    if event.type == pygame.KEYUP and event.key == ord('w'):
                        result = state.moveUp()
                    elif event.type == pygame.KEYDOWN and event.key == ord('s'):
                        result = state.moveDown()
                    elif event.type == pygame.KEYDOWN and event.key == ord('d'):
                        result = state.moveRight()
                    elif event.type == pygame.KEYDOWN and event.key == ord('a'):
                        result = state.moveLeft()
                    
                if display.quit(event):
                    return
            state.drawMaps()
            state.drawBox()
            #state.print_maps()
            display.update()

            if state.checkGoal():
                print("WINNER!")
                return
            if result == False:
                print("LOSER!")
                return
        else:
            if Algorithm is None:
                print("Error! Please read file README.md for more details. thanks")
                return
            else:
                node = TreeNode.TreeNode(state)
                if Algorithm == "bfs":
                   end_node =  bfs(node)
                   path = end_node.get_path()
                   
                       
                       #draw_path_3D(path, level=level, map_size=(size[0], size[1]))
                       



                
   

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
        main(level=Level.lv1, Play=False, Algorithm="bfs")