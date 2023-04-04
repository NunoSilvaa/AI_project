import pygame
import pygame_menu
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
    lv17 = "./level/17.json"

init_lv = Level.lv1
heuristic = "manhattan"

def draw_path_3D(solution, timesleep=0.5, level=Level.lv1, map_size = (0,0),display = None):
    if solution != None:

        
        choiselv = maps(level)


        choiselv.drawMaps()
        choiselv.currBox.drawBox()
        
        display.update() 

        for path in solution:
            choiselv.currBox.location = path
            choiselv.currBox.drawBox()
            choiselv.drawMaps()
            display.update()
            pygame.time.delay(420)
            
            
        return

    else:
        print("Unable to find path for maps!")
        print("Dir Level: %s" % level)
        return

def set_level(selected, level):
    global init_lv
    init_lv = level

def play_game():
    global init_lv
    Maps = maps(init_lv)
    control = Control(Maps)
    size = Maps.size
    display = Display(title='Roll Block', map_size=(size[0], size[1]))
    result = True

    while True:
        for event in pygame.event.get():
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
                surface = pygame.display.set_mode((800, 600))

                menu4 = pygame_menu.Menu('Success', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)

                menu4.add.label("WINNER!")
                menu4.add.button('Main Menu', main)
                menu4.add.button('Quit', pygame_menu.events.EXIT)
                menu4.mainloop(surface)
            if result == False:
                surface = pygame.display.set_mode((800, 600))

                menu5 = pygame_menu.Menu('Loss', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)

                menu5.add.label("LOSER!")
                menu5.add.button('Main Menu', main)
                menu5.add.button('Quit', pygame_menu.events.EXIT)
                menu5.mainloop(surface)

def end_menu_success(algorithm_name, time, moves):
    surface = pygame.display.set_mode((800, 600))

    menu3 = pygame_menu.Menu('Success', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)

    menu3.add.label(algorithm_name + " took " + str(time) + " seconds to complete.") 
    menu3.add.label("Completed in " + str(moves) + " moves.")
    menu3.add.button('Main Menu', main)
    menu3.add.button('Quit', pygame_menu.events.EXIT)
    menu3.mainloop(surface)

def set_heuristic(selected, heuristic_name):
    global heuristic
    heuristic = heuristic_name
            
def chose_algorithm():
    surface = pygame.display.set_mode((800, 600))
    menu2 = pygame_menu.Menu('Algorithms', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)

    menu2.add.selector('Heuristic :', 
                       [('Manhattan', "manhattan"), ('Terrain', "terrain"),
                       ('Edge', "edge"), ('Chebyshev', "chebyshev")],
                       onchange=set_heuristic)
    menu2.add.selector('Algorithm :', 
                       [('BFS', 1), ('DFS', 2),
                       ('IDDFS', 3), ('GREADY', 4),
                       ('UC', 5), ('A*', 6)], 
                       onreturn=do_algorithm)

    menu2.mainloop(surface)

def do_algorithm(selected, num):

    global init_lv
    global heuristic
    Maps = maps(init_lv)
    size = Maps.size
    display = Display(title='Roll Block', map_size=(size[0], size[1]))

    root = TreeNode.TreeNode(State(Maps.currBox.location,Maps))
    goal = TreeNode.TreeNode(State([Maps.end],Maps))

    start = time.time()
    end = 0
    if num == 1:
        solution = bfs(root, goal)
        end = time.time()
        if solution != None:
            path = solution.get_path()
            draw_path_3D(path, level=init_lv, map_size=(size[0], size[1]),display=display)
        
    elif num == 2:
        solution = dfs(root, goal)
        end = time.time()
        if solution != None:
            path = solution.get_path()
            draw_path_3D(path, level=init_lv, map_size=(size[0], size[1]),display=display)
        
    elif num == 3:
        solution = iddfs(root, goal,100 )
        end = time.time()
        if solution != None:
            path = solution.get_path()
            draw_path_3D(path, level=init_lv, map_size=(size[0], size[1]),display=display)
    
    elif num == 4:
        solution = greedy_search(root, goal, heuristic)
        end = time.time()
        if solution != None:
            path = solution.get_path()
            draw_path_3D(path, level=init_lv, map_size=(size[0], size[1]),display=display)
    elif num == 5:
        solution = uniform_cost_search(root,goal)
        end = time.time()
        if solution != None:
            path = solution.get_path()
            draw_path_3D(path, level=init_lv, map_size=(size[0], size[1]),display=display)
    elif num == 6:
            solution = a_star(root,goal, heuristic)
            end = time.time()
            if solution != None:
                path = solution.get_path()
                draw_path_3D(path, level=init_lv, map_size=(size[0], size[1]),display=display)

    pygame.display.flip()
    final_time = end - start
    end_menu_success(selected[0][0], final_time, len(solution.get_path()))


    
def main():
    pygame.init()
    surface = pygame.display.set_mode((800, 600))

    menu = pygame_menu.Menu('Roll Block', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)

    menu.add.selector('Level :', 
                      [('level 1', Level.lv1), ('level 2', Level.lv2),
                       ('level 3', Level.lv3), ('level 4', Level.lv4),
                       ('level 5', Level.lv5), ('level 6', Level.lv6),
                       ('level 7', Level.lv7), ('level 8', Level.lv8,),
                       ('level 9', Level.lv9), ('level 10', Level.lv10),
                       ('level 11', Level.lv11), ('level 12', Level.lv12),
                       ('level 13', Level.lv13), ('level 14', Level.lv14),
                       ('level 15', Level.lv15), ('level 16', Level.lv16),
                       ('level 17', Level.lv17)], 
                       onchange=set_level)
    menu.add.button('Play', play_game)
    menu.add.button('Algorithms', chose_algorithm)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)


if __name__=="__main__":
    main()
