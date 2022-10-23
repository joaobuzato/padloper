
import random
from player2 import Player2

class Player2Manager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = ['blue']
        self.spawn_positions = [{'x': 0, 'y': 50}]
        
        self.screen = screen
        
    def setup(self):
        pass

    def input(self):
        
        self.screen.onkeyrelease(key='t', fun=self.input_t)
        self.screen.onkeyrelease(key='g', fun=self.input_g)
        self.screen.onkeyrelease(key='f', fun=self.input_f)
        self.screen.onkeyrelease(key='h', fun=self.input_h)
        pass

    def update(self,start):
        
        if len(self.actor_list) == 0:
            actor = Player2(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
            self.actor_list.append(actor)
                
        pass
    
    
    def input_t(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    def input_g(self):
        for actor in self.actor_list:
            actor.backward(10)
            
    def input_f(self):
        for actor in self.actor_list:
            actor.left(10)
            
    def input_h(self):
        for actor in self.actor_list:
            actor.right(10)
            
    