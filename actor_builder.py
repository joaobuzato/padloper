from manager_builder import ManagerBuilder

class ActorBuilder:
    def __init__(self):
        self.actor = None
        self.manager_builder = ManagerBuilder()
        pass

    def build(self, actor):
        self.actor = actor
        
        self.manager_builder.build(actor)
        self.manager_setups = self.manager_builder.manager_setups
        self.input_setups = self.manager_builder.input_setups
        self.setup_setups = self.manager_builder.setup_setups
        self.update_setups = self.manager_builder.update_setups
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
        self.speed(8)
        self.shape("square")
        self.color(color)
        self.penup()
        self.padscreen = padscreen
        
        self.goto(position.get("x"), position.get("y"))
        self.st()

    def is_out_of_screen(self):
        if self.padscreen.left_x -50 > self.xcor() or self.xcor() > self.padscreen.right_x + 50:
            return True
        
        if self.padscreen.bottom_y -50 > self.ycor() or self.ycor() > self.padscreen.top_y + 50:
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
        if self.xcor()-10 <= object.xcor() <= self.xcor()+10 and self.ycor() -10 <= object.ycor() <= self.ycor() +10:
            return True
        else:
            return False
"""

        file = open(f"src/{self.actor.get('name')}.py", "w")
        file.write(actor_txt)
        file.close()

    