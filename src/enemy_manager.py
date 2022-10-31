
import random
from enemy import Enemy

class EnemyManager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = ['black', 'yellow', 'blue', 'red']
        self.spawn_positions = [{'x': 50, 'y': 0}, {'x': 100, 'y': 0}, {'x': 150, 'y': 0}, {'x': 200, 'y': 0}, {'x': -50, 'y': 0}, {'x': -100, 'y': 0}, {'x': -150, 'y': 0}, {'x': -200, 'y': 0}]
        
        self.screen = screen
        
    def check_collision(self, object_list):
        for actor in self.actor_list:
            for object in object_list:
                if actor.touches(object):
                    return True
                    
        return False
    def setup(self):
        pass

    def input(self):
        
        pass

    def update(self,start):
        
        self.update_forward()
                
        actor = Enemy(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
        self.actor_list.append(actor)
                
        pass
    
    
    def update_forward(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    