
import random
from enemy import Enemy

class EnemyManager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = ['black', 'yellow', 'blue', 'red']
        self.spawn_positions = [{'x': 510, 'y': 300}, {'x': 510, 'y': 250}, {'x': 510, 'y': 200}, {'x': 510, 'y': 150}, {'x': 510, 'y': 100}, {'x': 510, 'y': 50}, {'x': 510, 'y': 0}, {'x': 510, 'y': -50}, {'x': 510, 'y': -100}, {'x': 510, 'y': -150}, {'x': 510, 'y': -200}, {'x': 510, 'y': -250}, {'x': 510, 'y': -300}]
        
        self.screen = screen
        
    def check_collision(self, object_list):
        for actor in self.actor_list:
            for obj in object_list:
                if actor.touches(obj):
                    return True
                    
        return False
    def setup(self):
        pass

    def input(self):
        
        pass

    def update(self,start):
        
        self.update_strife_left()
                
        if len(self.actor_list) < 300:
            actor = Enemy(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
            self.actor_list.append(actor)
                
        pass
    
    
    def update_strife_left(self):
        for actor in self.actor_list:
            actor.setx(actor.xcor() - 10)
            
    