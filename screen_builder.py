
class ScreenBuilder:
    def __init__(self, name):
        self.game_name = name


        pass

    def build(self, screen):
        self.height = screen.get('height')
        self.width = screen.get('width')
        screen_txt = f""" 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.mode("logo")
        self.screen.setup(width={self.width}, height={self.height})
        self.top_x = {self.height/2}
        self.bottom_x = -{self.height/2}
        self.left_y = -{self.width/2}
        self.right_y = {self.width/2}
        self.screen.title('{self.game_name}')
        self.screen.tracer(0)

    def get_screen_obj(self):
        return self.screen
"""
        file = open("src/padscreen.py", "w")
        file.write(screen_txt)
        file.close()
