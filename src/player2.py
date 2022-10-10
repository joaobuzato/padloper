
from turtle import Turtle

class Player2 (Turtle):

    def __init__(self) :
        super().__init__()
        self.color('green')
        self.penup()
        self.goto(0,-50)
