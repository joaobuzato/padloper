import json

# json loads // json dumps
class GameBuilder:
    def __init__(self):
        self.game_map = json.loads(open('map.json').read())
        self.pad_main_txt = ""
        self.build_game()

    def build_game(self):
        self.create_screen()
        self.create_actors()
        self.create_main()
    def create_screen(self):
        screen = self.game_map.get("screen")

        screen_txt = f""" 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width={screen.get('width')}, height={screen.get('height')})
        self.screen.title('{self.game_map.get('name')}')

    def get_screen_obj(self):
        return self.screen
"""
        file = open("src/padscreen.py", "w")
        file.write(screen_txt)
        file.close()

    def create_actors(self):
        self.manager_setups = ""
        self.input_setups = ""
        for actor in self.game_map.get("actors"):
            class_name = str.title(actor.get("name"))
            self.pad_main_txt += f"""
from {actor.get("name")}_manager import {class_name}Manager"""
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

            self.manager_txt = f"""
from {actor.get("name")} import {class_name}

class {class_name}Manager():
    
    def __init__(self, screen):
        self.{actor.get("name")}_list = []
        self.actor = {class_name}()
        self.screen = screen
        
    def input(self):
"""
            if actor.get("behaviors").get("inputs") != None:
                functions_txt = ""
                for input in actor.get("behaviors").get("inputs"):
                    self.manager_txt += f"""
        self.screen.onkey(key='{input.get('key')}', fun=self.{input.get('key')})"""
                    functions_txt += f"""
    def {input.get("key")}(self):
        self.actor.{input.get("action")}({input.get("param")})
"""

                self.manager_txt += functions_txt

            self.manager_txt += """
        pass
"""

            self.manager_setups += f"""
        self.{actor.get("name")}_manager = {class_name}Manager(self.screen)"""
            self.input_setups += f"""
        self.{actor.get("name")}_manager.input()"""
            file = open(f"src/{actor.get('name')}_manager.py", "w")
            file.write(self.manager_txt)
            file.close()

    def create_main(self):
        self.pad_main_txt += f"""
import time
from padscreen import PadScreen

class PadMain():

    def __init__(self):
        padscreen = PadScreen()
        self.screen = padscreen.get_screen_obj()
        {self.manager_setups}
    
    def input(self):
        {self.input_setups}
        pass
    
    def update(self):
        pass
    
    def render(self):
        pass
        
    def game_loop(self):
        self.screen.listen()
        self.input()
        game_is_on = True
        while game_is_on:
            time.sleep(0.01)
            self.screen.update()
        
        self.screen.exitonclick()

pad_main = PadMain()
pad_main.game_loop()
"""

        file = open("src/padmain.py", "w")
        file.write(self.pad_main_txt)
        file.close()


GameBuilder()

