import pygame
import sys
import os
import time
from drawing.display import Display
from model.map import maps
from model.control import Control


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
    
    
def main(level=Level.lv1, Play=True, view='3'):
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
   

if __name__=="__main__":
    if len(sys.argv) > 2:
        level = sys.argv[1]
        option = sys.argv[2]
        if option != "play":
            view = sys.argv[3]
        if option == "play": 
            main(level=level, Play=True)

        else: 
            print("Error! Please read file README.md for more details. thanks")
    else:
        # Edit here
        main(level=Level.lv1, Play=True, view='3')