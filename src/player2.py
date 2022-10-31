
from turtle import Turtle

class Player2(Turtle):

    def __init__(self, color,position) :
        super().__init__()
        self.speed(8)
        self.shape("square")
        self.color(color)
        self.penup()
        self.ht()
        self.goto(position.get("x"), position.get("y"))
        self.st()
        
        
    def touches(self,object):
        if self.xcor()-10 <= object.xcor() <= self.xcor()+10 and self.ycor() -10 <= object.ycor() <= self.ycor() +10:
            return True
        else:
            return False
