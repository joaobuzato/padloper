
from turtle import Turtle

class Player2(Turtle):

    def __init__(self, color,position) :
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(position.get("x"), position.get("y"))
