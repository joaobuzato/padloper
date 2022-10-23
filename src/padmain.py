

    
from player_manager import PlayerManager
    
from player2_manager import Player2Manager
    
from enemy_manager import EnemyManager
import time
from timeit import default_timer as timer
from padscreen import PadScreen

class PadMain():

    def __init__(self):
        padscreen = PadScreen()
        self.screen = padscreen.get_screen_obj()
        
        self.player_manager = PlayerManager(self.screen)
        self.player2_manager = Player2Manager(self.screen)
        self.enemy_manager = EnemyManager(self.screen)
    def setup(self):
        
        self.player_manager.setup()
        self.player2_manager.setup()
        self.enemy_manager.setup()
        pass
    def input(self):
        
        self.player_manager.input()
        self.player2_manager.input()
        self.enemy_manager.input()
        pass
    
    def update(self,start):
        
        self.player_manager.update(start)
        self.player2_manager.update(start)
        self.enemy_manager.update(start)
        pass
    
    def render(self):
        time.sleep(0.01)
        self.screen.update()
        pass
        
    def game_loop(self):
        start = timer()
        self.screen.listen()
        self.setup()
        self.input()
        game_is_on = True
        while game_is_on:
            self.update(start)
            self.render()
        
        self.screen.mainloop()

pad_main = PadMain()
pad_main.game_loop()
