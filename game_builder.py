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


for actor in game_map.get("actors"):
    class_name = str.title(actor.get("name"))
    actor_txt = f"""
from turtle import Turtle

class {class_name} (Turtle):
    
    def __init__(self) :
        super().__init__()
        self.penup()
        self.goto({actor.get("components").get("pos").get("x")},{actor.get("components").get("pos").get("y")})
        self.color('{actor.get("components").get("color")}')
"""

    file = open(f"src/{actor.get('name')}.py", "w")
    file.write(actor_txt)
    file.close()

    manager_txt = f"""
from turtle import Turtle
from {actor.get("name")} import {class_name}

class {class_name}Manager(Turtle):
    
    def __init__(self, screen):
        super().__init__()
        self.{actor.get("name")}_list = []
        self.screen = screen
        
    def input(self):
"""
    if actor.get("behaviors").get("inputs") != None:

        for input in actor.get("behaviors").get("inputs"):
            manager_txt += f"""
        self.screen.onkey(key='{input.get('key')}', fun=self.{input.get('key')})"""
    manager_txt += """
        pass
"""

    file = open(f"src/{actor.get('name')}_manager.py", "w")
    file.write(manager_txt)
    file.close()


pad_main_txt = f"""
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

file = open("src/padmain.py", "w")
file.write(pad_main_txt)
file.close()

