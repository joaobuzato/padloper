import json

# json loads // json dumps

game_map = json.loads(open('map.json').read())

print(game_map.get("screen"))
screen = game_map.get("screen")
screen_txt = f""" 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width={screen.get('width')}, height={screen.get('height')})
        self.screen.title('{game_map.get('name')}')

    def get_screen_obj(self):
        return self.screen
"""
file = open("src/padscreen.py", "w")
file.write(screen_txt)
file.close()

main_game_txt = f"""
import time
from padscreen import PadScreen

class PadMain():

    def __init__(self):
        padscreen = PadScreen()
        self.screen = padscreen.get_screen_obj()
    
    def input(self):
        pass
    
    def update(self):
        pass
    
    def render(self):
        pass
        
    def game_loop(self):
        game_is_on = True
        while game_is_on:
            time.sleep(0.01)
            self.screen.update()
        
        self.screen.exitonclick()

pad_main = PadMain()
pad_main.game_loop()
"""

file = open("src/game_main.py", "w")
file.write(main_game_txt)
file.close()

