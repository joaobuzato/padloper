
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.ht()
        self.penup()
        self.color("Black")
        self.goto((0, 470.0))
        self.write(f"Placar: " + str(self.score) +" Pontos" , align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto((0, 470.0))
        self.write(f"Placar: "+ str(self.score) +" Pontos", align=ALIGNMENT, font=FONT)

    def game_won(self):
        self.clear()
        self.goto(0,0)
        self.write(f"VOCE VENCEU! - PLACAR: "+str(self.score)+" Pontos", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER - PLACAR: "+str(self.score) + " Pontos", align=ALIGNMENT, font=FONT)
