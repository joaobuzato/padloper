
from player2 import Player2

class Player2Manager():

    def __init__(self, screen):
        self.player2_list = []
        self.actor = Player2()
        self.screen = screen

    def input(self):

        self.screen.onkey(key='e', fun=self.e)
        self.screen.onkey(key='d', fun=self.d)
    def e(self):
        self.actor.fd(10)
        
    def d(self):
        self.actor.bk(10)
        
        pass
        