
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
    def w(self):
        for actor in self.actor_list:
            actor.fd(10)
        
    def s(self):
        for actor in self.actor_list:
            actor.bk(10)
        
        pass
        