
class ScreenBuilder:
    def __init__(self, name):
        self.game_name = name


        pass

    def build(self, screen):
        self.screen = screen
        self.height = self.screen.get('height')
        self.width = self.screen.get('width')
        screen_txt = f""" 
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.mode("logo")
        self.screen.setup(width={self.width}, height={self.height})
        self.screen.bgcolor("{self.screen.get("color")}")
        self.top_y = {self.height/2}
        self.bottom_y = -{self.height/2}
        self.left_x = -{self.width/2}
        self.right_x = {self.width/2}
        self.screen.title('{self.game_name}')
        self.screen.tracer(0)

    def get_screen_obj(self):
        return self.screen
"""
        file = open("src/padscreen.py", "w")
        file.write(screen_txt)
        file.close()
