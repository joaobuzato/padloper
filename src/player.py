
from turtle import Turtle

class Player(Turtle):

    def __init__(self) :
        super().__init__()
        self.color('red')
        self.penup()
        self.goto(0,50)
