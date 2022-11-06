
import random
from player2 import Player2

class Player2Manager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = ['blue']
        self.spawn_positions = [{'x': 0, 'y': 50}]
        
        self.screen = screen
        
    def check_collision(self, object_list):
        collision = {"has_collision" : False}
        for actor in self.actor_list:
            for obj in object_list:
                if actor.touches(obj):
                    collision = {
                        "has_collision": True,
                        "actor1" : actor,
                        "actor2" : obj
                    }
                    return collision
                    
        return collision

    def check_position(self, **kwargs):
        x_pos = kwargs.get("x_pos")
        y_pos = kwargs.get("y_pos")
        x_cond = kwargs.get("x_cond")
        y_cond = kwargs.get("y_cond")
        for actor in self.actor_list:
            if x_pos is None:
                if actor.check_y_position(y_pos,y_cond):
                    return { "position_checked" : True, "actor" : actor}
            elif y_pos is None:
                if actor.check_x_position(x_pos,x_cond):
                    return { "position_checked" : True, "actor" : actor}
            else:
                if actor.check_y_position(y_pos, y_cond) and actor.check_x_position(x_pos, x_cond):
                    return { "position_checked" : True, "actor" : actor}

        return { "position_checked" : False }
        
        
    def setup(self):
        pass

    def input(self):
        
        self.screen.onkeyrelease(key='t', fun=self.func_forward)
        self.screen.onkeyrelease(key='g', fun=self.func_backward)
        self.screen.onkeyrelease(key='f', fun=self.func_left)
        self.screen.onkeyrelease(key='h', fun=self.func_right)
        pass

    def update(self,start):
        
        if len(self.actor_list) == 0:
            actor = Player2(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
            self.actor_list.append(actor)
                
        pass
    
    
    def func_forward(self):
        for actor in self.actor_list:
        
            actor.forward(10)
            
    def func_backward(self):
        for actor in self.actor_list:
        
            actor.backward(10)
            
    def func_left(self):
        for actor in self.actor_list:
        
            actor.left(10)
            
    def func_right(self):
        for actor in self.actor_list:
        
            actor.right(10)
            
    