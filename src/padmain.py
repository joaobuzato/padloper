

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
    
    def input(self):
        
        self.player_manager.input()
        self.player2_manager.input()
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
