
import random
from player import Player

class PlayerManager():

    def __init__(self, padscreen):
        self.actor_list = []
        self.spawn_colors = ['red']
        self.spawn_positions = [{'x': 0, 'y': 470}]
        
        self.padscreen = padscreen

    def remove_actor(self,actor):
        actor.goto(10000,10000)
        self.actor_list.remove(actor)
        
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
        
        self.padscreen.get_screen_obj().onkeyrelease(key='w', fun=self.func_forward)
        self.padscreen.get_screen_obj().onkeyrelease(key='s', fun=self.func_backward)
        self.padscreen.get_screen_obj().onkeyrelease(key='a', fun=self.func_strife_left)
        self.padscreen.get_screen_obj().onkeyrelease(key='d', fun=self.func_strife_right)
        pass

    def update(self,screen_updates):
        
        if  None == None or (screen_updates >= None and screen_updates%None == 0):
            

            if len(self.actor_list) == 0:
                actor = Player(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)), padscreen=self.padscreen)
                self.actor_list.append(actor)
                    
        pass
    
    
    def func_forward(self):
        for actor in self.actor_list:
            if actor.is_out_of_screen():
                self.remove_actor(actor)
        
            actor.forward(10)
            
    def func_backward(self):
        for actor in self.actor_list:
            if actor.is_out_of_screen():
                self.remove_actor(actor)
        
            actor.backward(10)
            
    def func_strife_left(self):
        for actor in self.actor_list:
            if actor.is_out_of_screen():
                self.remove_actor(actor)
        
            actor.setx(actor.xcor() - 10)
            
    def func_strife_right(self):
        for actor in self.actor_list:
            if actor.is_out_of_screen():
                self.remove_actor(actor)
        
            actor.setx(actor.xcor() + 10)
        
    