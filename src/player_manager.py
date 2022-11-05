
import random
from player import Player

class PlayerManager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = ['red']
        self.spawn_positions = [{'x': 0, 'y': 0}]
        
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
        
        self.screen.onkeyrelease(key='w', fun=self.input_w)
        self.screen.onkeyrelease(key='s', fun=self.input_s)
        self.screen.onkeyrelease(key='a', fun=self.input_a)
        self.screen.onkeyrelease(key='d', fun=self.input_d)
        pass

    def update(self,start):
        
        if len(self.actor_list) == 0:
            actor = Player(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
            self.actor_list.append(actor)
                
        pass
    
    
    def input_w(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    def input_s(self):
        for actor in self.actor_list:
            actor.backward(10)
            
    def input_a(self):
        for actor in self.actor_list:
            actor.setx(actor.xcor() - 10)
            
    def input_d(self):
        for actor in self.actor_list:
            actor.setx(actor.xcor() + 10)
            
    