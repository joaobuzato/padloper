
from turtle import Turtle
from player import Player

class PlayerManager(Turtle):
    
    def __init__(self, screen):
        super().__init__()
        self.player_list = []
        self.screen = screen
        
    def input(self):

        self.screen.onkey(key='w', fun=self.w)
        self.screen.onkey(key='s', fun=self.s)
        pass
