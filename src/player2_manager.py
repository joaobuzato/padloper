
from player2 import Player2

class Player2Manager():

    def __init__(self, screen):
        self.actor_list = []
        
        self.screen = screen
        
    def setup(self):
        actor = Player2()
        self.actor_list.append(actor)

    def input(self):
        
        self.screen.onkey(key='t', fun=self.t)
        self.screen.onkey(key='g', fun=self.g)
        self.screen.onkey(key='f', fun=self.f)
        self.screen.onkey(key='h', fun=self.h)
        pass
        
    
    def t(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    def g(self):
        for actor in self.actor_list:
            actor.backward(10)
            
    def f(self):
        for actor in self.actor_list:
            actor.left(10)
            
    def h(self):
        for actor in self.actor_list:
            actor.right(10)
            
        