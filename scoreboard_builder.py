class ScoreboardBuilder:

    def __init__(self,screen,scoreboard):
        self.screen = screen
        self.scoreboard = scoreboard
        pass


    def build(self):
        position = self.scoreboard.get("position")
        if position == "top":
            coordinates = (0, self.screen.get("height")/2 - 30)
        if position == "bottom":
            coordinates = (0, -self.screen.get("height")/2 + 30)
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
        self.goto({coordinates})
        self.write(f"Score: " + str(self.score), align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto({coordinates})
        self.write(f"Score: "+ str(self.score), align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER - Score: "+str(self.score), align=ALIGNMENT, font=FONT)
"""


        file = open("src/scoreboard.py", "w")
        file.write(self.scoreboard_txt)
        file.close()
        