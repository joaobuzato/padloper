
import random
from enemy import Enemy

class EnemyManager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = ['black', 'yellow', 'blue', 'red']
        self.spawn_positions = [{'x': 510, 'y': 300}, {'x': 510, 'y': 250}, {'x': 510, 'y': 200}, {'x': 510, 'y': 150}, {'x': 510, 'y': 100}, {'x': 510, 'y': 50}, {'x': 510, 'y': 0}, {'x': 510, 'y': -50}, {'x': 510, 'y': -100}, {'x': 510, 'y': -150}, {'x': 510, 'y': -200}, {'x': 510, 'y': -250}, {'x': 510, 'y': -300}]
        
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
        
        pass

    def update(self,start):
        
        self.func_strife_left()
                
        if len(self.actor_list) < 300:
            actor = Enemy(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
            self.actor_list.append(actor)
                
        pass
    
    
    def func_strife_left(self):
        for actor in self.actor_list:
        
            actor.setx(actor.xcor() - 10)
            
    