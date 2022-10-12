
from player import Player

class PlayerManager():

    def __init__(self, screen):
        self.actor_list = []
        
        self.screen = screen
        
    def setup(self):
        actor = Player()
        self.actor_list.append(actor)

    def input(self):
        
        self.screen.onkey(key='w', fun=self.w)
        self.screen.onkey(key='s', fun=self.s)
        self.screen.onkey(key='a', fun=self.a)
        self.screen.onkey(key='d', fun=self.d)
        pass
        
    
    def w(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    def s(self):
        for actor in self.actor_list:
            actor.backward(10)
            
    def a(self):
        for actor in self.actor_list:
            actor.left(10)
            
    def d(self):
        for actor in self.actor_list:
            actor.right(10)
            
        