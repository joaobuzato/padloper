import json
from screen_builder import ScreenBuilder
from actor_builder import ActorBuilder
from rule_builder import RuleBuilder

# json loads // json dumps
class GameBuilder:
    def __init__(self):
        self.game_map = json.loads(open('map.json').read())
        self.screen_builder = ScreenBuilder(self.game_map.get("name"))
        self.actor_builder = ActorBuilder()
        self.rule_builder = RuleBuilder(self.game_map.get("rules"))
        self.pad_main_txt = ""
        self.manager_imports_txt = ""
        self.build_game()

    def build_game(self):
        self.create_screen()
        self.create_actors()
        self.create_rules()
        self.create_main()
    def create_screen(self):
        screen = self.game_map.get("screen")
        self.screen_builder.build(screen)

    def create_rules(self):
        self.rule_builder.build()
        self.rules_setups = self.rule_builder.rules_setups

    def create_actors(self):

        self.manager_setups = ""
        self.input_setups = ""
        for actor in self.game_map.get("actors"):
            self.actor_builder.build(actor)

        self.manager_setups = self.actor_builder.manager_setups
        self.input_setups = self.actor_builder.input_setups
        self.update_setups = self.actor_builder.update_setups
        self.setup_setups = self.actor_builder.setup_setups
        self.manager_imports = self.actor_builder.manager_imports

    def create_main(self):
        self.pad_main_txt += f"""
{self.manager_imports}
import time
from timeit import default_timer as timer
from padscreen import PadScreen

class PadMain():

    def __init__(self):
        self.game_is_on = False
        self.padscreen = PadScreen()
        self.screen = self.padscreen.get_screen_obj()
        {self.manager_setups}
    def setup(self):
        {self.setup_setups}
        pass
    def input(self):
        {self.input_setups}
        pass
    
    def update(self,start):
        {self.update_setups}
        pass
    
    def render(self):
        time.sleep(0.01)
        self.screen.update()
        pass
    
    def rules(self):
        {self.rules_setups}
        pass
        
    def game_loop(self):
        start = timer()
        self.screen.listen()
        self.setup()
        self.input()
        self.game_is_on = True
        while self.game_is_on:
            self.rules()
            self.update(start)
            self.render()
        
        self.screen.mainloop()

pad_main = PadMain()
pad_main.game_loop()
"""

        file = open("src/padmain.py", "w")
        file.write(self.pad_main_txt)
        file.close()


GameBuilder()

