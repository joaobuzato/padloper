
class ScreenBuilder:
    def __init__(self, name):
        self.game_name = name
        pass

    def build(self, screen):
        screen_txt = f""" 
        
        
        
from turtle import Screen

class PadScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.mode("logo")
        self.screen.setup(width={screen.get('width')}, height={screen.get('height')})
        self.screen.title('{self.game_name}')

    def get_screen_obj(self):
        return self.screen
"""





        file = open("src/padscreen.py", "w")
        file.write(screen_txt)
        file.close()
