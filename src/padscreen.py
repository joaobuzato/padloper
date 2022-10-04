 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1000, height=1000)
        self.screen.title('Projeto de Jogo')

    def get_screen_obj(self):
        return self.screen
