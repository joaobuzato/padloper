
from turtle import Turtle

class Enemy(Turtle):

    def __init__(self) :
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color('black')
        self.penup()
        self.goto(20,20)
