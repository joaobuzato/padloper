

class ActorBuilder:
    def __init__(self):
        self.actor = None
        self.manager_setups = ""
        self.input_setups = ""
        self.manager_imports = ""
        self.class_name = ""
        pass

    def build(self, actor):
        self.actor = actor
        self.build_actor()
        self.build_manager()
        pass

    def build_actor(self):
        self.class_name = str.title(self.actor.get("name"))
        actor_txt = f"""
from turtle import Turtle

class {self.class_name} (Turtle):

    def __init__(self) :
        super().__init__()
        self.color('{self.actor.get("components").get("color")}')
        self.penup()
        self.goto({self.actor.get("components").get("pos").get("x")},{self.actor.get("components").get("pos").get("y")})
"""

        file = open(f"src/{self.actor.get('name')}.py", "w")
        file.write(actor_txt)
        file.close()

    def build_manager(self):
        self.manager_txt = f"""
from {self.actor.get("name")} import {self.class_name}

class {self.class_name}Manager():

    def __init__(self, screen):
        self.{self.actor.get("name")}_list = []
        self.actor = {self.class_name}()
        self.screen = screen

    def input(self):
"""
        if self.actor.get("behaviors").get("inputs") != None:
            functions_txt = ""
            for input in self.actor.get("behaviors").get("inputs"):
                self.manager_txt += f"""
        self.screen.onkey(key='{input.get('key')}', fun=self.{input.get('key')})"""
                functions_txt += f"""
    def {input.get("key")}(self):
        self.actor.{input.get("action")}({input.get("param")})
        """
            self.manager_txt += functions_txt
        self.manager_txt += """
        pass
        """
        self.manager_imports += f"""
        
from {self.actor.get("name")}_manager import {self.class_name}Manager"""

        self.manager_setups += f"""
        self.{self.actor.get("name")}_manager = {self.class_name}Manager(self.screen)"""
        self.input_setups += f"""
        self.{self.actor.get("name")}_manager.input()"""
        file = open(f"src/{self.actor.get('name')}_manager.py", "w")
        file.write(self.manager_txt)
        file.close()
        pass