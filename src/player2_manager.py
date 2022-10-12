
from player2 import Player2

class Player2Manager():

    def __init__(self, screen):
        self.actor_list = []
        
        self.screen = screen
        
    def setup(self):
        actor = Player2()
        self.actor_list.append(actor)

    def input(self):
        
        self.screen.onkey(key='e', fun=self.e)
        self.screen.onkey(key='d', fun=self.d)
        pass
        
    
    def e(self):
        for actor in self.actor_list:
            actor.fd(10)
        
    def d(self):
        for actor in self.actor_list:
            actor.bk(10)
        
        