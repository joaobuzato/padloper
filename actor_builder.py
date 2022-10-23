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

    def __init__(self) :
        super().__init__()
        self.color('{self.actor.get("components").get("color")}')
        self.penup()
        self.goto({self.actor.get("components").get("pos").get("x")},{self.actor.get("components").get("pos").get("y")})
"""

        file = open(f"src/{self.actor.get('name')}.py", "w")
        file.write(actor_txt)
        file.close()

    