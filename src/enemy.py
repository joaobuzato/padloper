
from turtle import Turtle

class Enemy(Turtle):

    def __init__(self, color,position) :
        super().__init__()
        self.ht()
        self.speed(8)
        self.shape("square")
        self.color(color)
        self.penup()
        
        self.goto(position.get("x"), position.get("y"))
        self.st()
        
        
    def check_y_position(self, position, condition ):
        if condition == "greater" and self.ycor() > position:
            return True
        if condition == "lesser" and self.ycor() < position:
            return True
        if condition == "equals" and self.ycor() == position:
            return True

        return False

    def check_x_position(self, position, condition ):
        if condition == "greater" and self.xcor() > position:
            return True
        if condition == "lesser" and self.xcor() < position:
            return True
        if condition == "equals" and self.xcor() == position:
            return True

        return False


    def touches(self,object):
        if self.xcor()-10 <= object.xcor() <= self.xcor()+10 and self.ycor() -10 <= object.ycor() <= self.ycor() +10:
            return True
        else:
            return False
