
from turtle import Turtle

class Player (Turtle):
    
    def __init__(self) :
        super().__init__()
        self.penup()
        self.goto(0,50)
        self.color('red')
