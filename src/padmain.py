

    
from player_manager import PlayerManager
    
from ball_manager import BallManager
    
from enemy_manager import EnemyManager
import time
from timeit import default_timer as timer
from padscreen import PadScreen
from scoreboard import Scoreboard

class PadMain():

    def __init__(self):
        self.game_is_on = False
        self.padscreen = PadScreen()
        self.screen = self.padscreen.get_screen_obj()
        self.scoreboard = Scoreboard()
        
        self.player_manager = PlayerManager(self.padscreen)
        self.ball_manager = BallManager(self.padscreen)
        self.enemy_manager = EnemyManager(self.padscreen)
    def setup(self):

        
        self.player_manager.setup()
        self.ball_manager.setup()
        self.enemy_manager.setup()
        pass
    def input(self):
        
        self.player_manager.input()
        self.ball_manager.input()
        self.enemy_manager.input()
        pass
    
    def update(self,screen_updates):
        
        self.player_manager.update(screen_updates)
        self.ball_manager.update(screen_updates)
        self.enemy_manager.update(screen_updates)
        pass
    
    def render(self):
        time.sleep(0.03)
        self.screen.update()
        pass
    
    def rules(self):
        
        obj = self.ball_manager.check_position(y_pos=480,x_pos=None, y_cond='greater',x_cond='None')
        if obj.get("position_checked"):
                
                obj.get("actor").bounce_y()
                    
        obj = self.ball_manager.check_position(y_pos=-480,x_pos=None, y_cond='lesser',x_cond='None')
        if obj.get("position_checked"):
                
                obj.get("actor").bounce_y()
                    
        obj = self.ball_manager.check_position(y_pos=None,x_pos=-480, y_cond='None',x_cond='lesser')
        if obj.get("position_checked"):
                
                obj.get("actor").bounce_x()
                    
        obj = self.ball_manager.check_position(y_pos=None,x_pos=480, y_cond='None',x_cond='greater')
        if obj.get("position_checked"):
                
                obj.get("actor").bounce_x()
                    
        if self.scoreboard.score >= 3 :    
                
                self.scoreboard.game_won()
                self.game_is_on = False
                
        obj = self.player_manager.check_collision(self.enemy_manager.actor_list)
        if obj.get('has_collision'):
        
                self.scoreboard.game_over()
                self.game_is_on = False
                
        obj = self.player_manager.check_position(y_pos=480,x_pos=None, y_cond='greater',x_cond='None')
        if obj.get("position_checked"):
                
                self.scoreboard.point()  
                
                obj.get("actor").goto((0, -480))
                
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
