
import random
from enemy import Enemy

class EnemyManager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = ['black', 'yellow', 'blue', 'red']
        self.spawn_positions = [{'x': 0, 'y': 0}, {'x': 50, 'y': 0}, {'x': 100, 'y': 0}, {'x': 150, 'y': 0}, {'x': 200, 'y': 0}]
        
        self.screen = screen
        
    def setup(self):
        pass

    def input(self):
        
        pass

    def update(self,start):
        
        self.update_space_invader()
                
        actor = Enemy(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
        self.actor_list.append(actor)
                
        pass
    
    
    def update_space_invader(self):
        for actor in self.actor_list:
            actor.setheading(90)
            actor.forward(20)
            actor.setheading(270)
            actor.forward(30)
            actor.setheading(180)
            actor.forward(10)
            actor.setheading(90)
            
    