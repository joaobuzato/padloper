from manager_builder import ManagerBuilder

class ActorBuilder:
    def __init__(self):
        self.actor = None
        self.manager_builder = ManagerBuilder()
        pass

    def build(self, actor):
        self.actor = actor
        self.manager_builder.build(actor)
        self.setups = self.manager_builder.setups
        self.manager_imports = self.manager_builder.manager_imports
        self.build_actor()
        pass

    def build_actor(self):
        self.class_name = str.title(self.actor.get("name"))
        actor_txt = f"""
from turtle import Turtle

class {self.class_name}(Turtle):

    def __init__(self, color,position,padscreen) :
        super().__init__()
        self.ht()
        self.speed({self.actor.get("components").get("speed")})
        self.setheading({self.actor.get("components").get("heading")})
        self.shape("square")
        self.resizemode("user")
        self.shapesize({self.actor.get("components").get("size")},{self.actor.get("components").get("size")})
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
        if self.distance(object) <= 10*{self.actor.get("components").get("size")}:
            return True
        else:
            return False
"""

        file = open(f"src/{self.actor.get('name')}.py", "w")
        file.write(actor_txt)
        file.close()

    