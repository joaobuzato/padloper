
from turtle import Turtle

class Enemy (Turtle):

    def __init__(self) :
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(20,20)
