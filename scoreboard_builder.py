class ScoreboardBuilder:

    def __init__(self,screen,scoreboard):
        self.screen = screen
        self.scoreboard = scoreboard
        pass


    def build(self):
        self.scoreboard_txt = f"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.ht()
        self.penup()
        self.color("black")
        self.goto(0, 120)
        self.write(f"Score: " + str(self.score), align=ALIGNMENT, font=FONT)

    def point(self):
        print("point!")
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 120)
        self.write(f"Score: "+ str(self.score), align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER - Score: "+str(self.score), align=ALIGNMENT, font=FONT)
"""


        file = open("src/scoreboard.py", "w")
        file.write(self.scoreboard_txt)
        file.close()
        