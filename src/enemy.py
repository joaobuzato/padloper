
from turtle import Turtle

class Enemy(Turtle):

    def __init__(self, color,position,padscreen) :
        super().__init__()
        self.ht()
        self.speed(10)
        self.setheading(270)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(1,1)
        self.color(color)
        self.penup()
        self.padscreen = padscreen
        self.goto(position.get("x"), position.get("y"))
        self.st()

    def bounce_x(self):
        self.setheading(360 - self.heading())
    
    def bounce_y(self):
        heading = self.heading()
        if heading < 180:
            self.setheading( 180 - heading)
        else: 
            self.setheading(540 - heading )

    def is_out_of_screen(self):
        if self.padscreen.left_x -200 > self.xcor() or self.xcor() > self.padscreen.right_x + 200:
            return True
        
        if self.padscreen.bottom_y -200 > self.ycor() or self.ycor() > self.padscreen.top_y + 200:
            return True 

        return False
        
        
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
        if self.distance(object) <= 10*None:
            return True
        else:
            return False
