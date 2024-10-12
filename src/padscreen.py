 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.mode("logo")
        self.screen.setup(width=500, height=500)
        self.screen.bgcolor("black")
        self.top_y = 250.0
        self.bottom_y = -250.0
        self.left_x = -250.0
        self.right_x = 250.0
        self.screen.title('Jogo Teste')
        self.screen.tracer(0)

    def get_screen_obj(self):
        return self.screen
