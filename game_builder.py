import json
from screen_builder import ScreenBuilder
from actor_builder import ActorBuilder

# json loads // json dumps
class GameBuilder:
    def __init__(self):
        self.game_map = json.loads(open('map.json').read())
        self.screen_builder = ScreenBuilder(self.game_map.get("name"))
        self.actor_builder = ActorBuilder()
        self.pad_main_txt = ""
        self.manager_imports_txt = ""
        self.build_game()

    def build_game(self):
        self.create_screen()
        self.create_actors()
        self.create_main()
    def create_screen(self):
        screen = self.game_map.get("screen")
        self.screen_builder.build(screen)

    def create_actors(self):

        self.manager_setups = ""
        self.input_setups = ""
        for actor in self.game_map.get("actors"):
            self.actor_builder.build(actor)

        self.manager_setups = self.actor_builder.manager_setups
        self.input_setups = self.actor_builder.input_setups
        self.manager_imports = self.actor_builder.manager_imports

    def create_main(self):
        self.pad_main_txt += f"""
{self.manager_imports}
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

