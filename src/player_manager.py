
from player import Player

class PlayerManager():

    def __init__(self, screen):
        self.actor_list = []
        
        self.screen = screen
        
    def setup(self):
        actor = Player()
        self.actor_list.append(actor)

    def input(self):
        
        self.screen.onkey(key='w', fun=self.input_w)
        self.screen.onkey(key='s', fun=self.input_s)
        self.screen.onkey(key='a', fun=self.input_a)
        self.screen.onkey(key='d', fun=self.input_d)
        pass
    
    def update(self):
        
        self.update_forward()
                
        self.update_right()
                
        pass
        
    
    def input_w(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    def input_s(self):
        for actor in self.actor_list:
            actor.backward(10)
            
    def input_a(self):
        for actor in self.actor_list:
            actor.left(10)
            
    def input_d(self):
        for actor in self.actor_list:
            actor.right(10)
            
    def update_forward(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    def update_right(self):
        for actor in self.actor_list:
            actor.right(10)
            
        