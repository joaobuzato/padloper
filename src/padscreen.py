 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.mode("logo")
        self.screen.setup(width=1000, height=1000)
        self.screen.bgcolor("green")
        self.top_y = 500.0
        self.bottom_y = -500.0
        self.left_x = -500.0
        self.right_x = 500.0
        self.screen.title('Projeto de Jogo')
        self.screen.tracer(0)

    def get_screen_obj(self):
        return self.screen
