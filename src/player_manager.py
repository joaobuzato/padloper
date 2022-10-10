
from player import Player

class PlayerManager():

    def __init__(self, screen):
        self.player_list = []
        self.actor = Player()
        self.screen = screen

    def input(self):

        self.screen.onkey(key='w', fun=self.w)
        self.screen.onkey(key='s', fun=self.s)
    def w(self):
        self.actor.fd(10)
        
    def s(self):
        self.actor.bk(10)
        
        pass
        