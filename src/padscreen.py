 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.mode("logo")
        self.screen.setup(width=1000, height=1000)
        self.top_x = 500.0
        self.bottom_x = -500.0
        self.left_y = -500.0
        self.right_y = 500.0
        self.screen.title('Projeto de Jogo')

    def get_screen_obj(self):
        return self.screen
