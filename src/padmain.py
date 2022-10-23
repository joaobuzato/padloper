

        
from player_manager import PlayerManager
        
from player2_manager import Player2Manager
import time
from padscreen import PadScreen

class PadMain():

    def __init__(self):
        padscreen = PadScreen()
        self.screen = padscreen.get_screen_obj()
        
        self.player_manager = PlayerManager(self.screen)
        self.player2_manager = Player2Manager(self.screen)
    def setup(self):
        
        self.player_manager.setup()
        self.player2_manager.setup()
        pass
    def input(self):
        
        self.player_manager.input()
        self.player2_manager.input()
        pass
    
    def update(self):
        
        self.player_manager.update()
        self.player2_manager.update()
        pass
    
    def render(self):
        time.sleep(0.1)
        self.screen.update()
        pass
        
    def game_loop(self):
        self.screen.listen()
        self.setup()
        self.input()
        game_is_on = True
        while game_is_on:
            self.update()
            self.render()
        
        self.screen.exitonclick()

pad_main = PadMain()
pad_main.game_loop()
