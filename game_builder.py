import json
from scoreboard_builder import ScoreboardBuilder
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
        self.scoreboard_builder = ScoreboardBuilder(self.game_map.get("screen"), self.game_map.get("scoreboard"))
        self.pad_main_txt = ""
        self.manager_imports_txt = ""
        self.build_game()

    def build_game(self):
        self.create_screen()
        self.create_actors()
        self.create_rules()
        self.create_scoreboard()
        self.create_main()
    def create_screen(self):
        screen = self.game_map.get("screen")
        self.screen_builder.build(screen)

    def create_scoreboard(self):
        self.scoreboard_builder.build()

    def create_rules(self):
        self.rule_builder.build()
        self.rules_setups = self.rule_builder.rules_setups

    def create_actors(self):

        self.manager_setups = ""
        self.input_setups = ""
        for actor in self.game_map.get("actors"):
            self.actor_builder.build(actor)

        self.actor_setups = self.actor_builder.setups

        # self.manager_setups = self.actor_builder.manager_setups
        # self.input_setups = self.actor_builder.input_setups
        # self.update_setups = self.actor_builder.update_setups
        # self.setup_setups = self.actor_builder.setup_setups
        self.manager_imports = self.actor_builder.manager_imports

    def create_main(self):
        self.pad_main_txt += f"""
{self.manager_imports}
import time
from timeit import default_timer as timer
from padscreen import PadScreen
from scoreboard import Scoreboard

class PadMain():

    def __init__(self):
        self.game_is_on = False
        
        
    def setup(self):
        self.padscreen = PadScreen()
        self.screen = self.padscreen.get_screen_obj()
        self.scoreboard = Scoreboard()
        {self.actor_setups.get("manager_setups")}
        pass
    def input(self):
        {self.actor_setups.get("input_setups")}
        pass
    
    def update(self,screen_updates):
        {self.actor_setups.get("update_setups")}
        pass
    
    def render(self):
        time.sleep(0.03)
        self.screen.update()
        pass
    
    def rules(self):
        {self.rules_setups}
        pass
        
    def game_loop(self):
        screen_updates = 0
        start = timer()
        self.setup()
        self.input()
        self.screen.listen()
        self.game_is_on = True
        while self.game_is_on:
            
            self.update(screen_updates)
            self.render()
            self.rules()
            screen_updates += 1
            
            
        
        self.screen.mainloop()

pad_main = PadMain()
pad_main.game_loop()
"""

        file = open("src/padmain.py", "w")
        file.write(self.pad_main_txt)
        file.close()


GameBuilder()

