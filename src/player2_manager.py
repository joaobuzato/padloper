
from player2 import Player2

class Player2Manager():

    def __init__(self, screen):
        self.actor_list = []
        
        self.screen = screen
        
    def setup(self):
        actor = Player2()
        self.actor_list.append(actor)

    def input(self):
        
        self.screen.onkey(key='t', fun=self.input_t)
        self.screen.onkey(key='g', fun=self.input_g)
        self.screen.onkey(key='f', fun=self.input_f)
        self.screen.onkey(key='h', fun=self.input_h)
        pass

    def update(self):
        
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
            
    