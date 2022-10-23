
from turtle import Turtle

class Player(Turtle):

    def __init__(self) :
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color('red')
        self.penup()
        self.goto(0,50)
