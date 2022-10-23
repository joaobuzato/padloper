
from turtle import Turtle

class Player2(Turtle):

    def __init__(self) :
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color('green')
        self.penup()
        self.goto(0,-50)
