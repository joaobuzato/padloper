
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
