

class ManagerBuilder:
    def __init__(self):
        self.actor = None
        self.manager_setups = ""
        self.input_setups = ""
        self.setup_setups = ""
        self.update_setups = ""
        self.manager_imports = ""
        self.class_name = ""
        pass

    def build_inputs(self):
        self.input_txt = ""

        if self.actor.get("behaviors").get("inputs") != None:
            for input in self.actor.get("behaviors").get("inputs"):
                self.input_txt += f"""
        self.screen.onkeyrelease(key='{input.get('key')}', fun=self.input_{input.get('key')})"""
                # TODO fazer inputs mais inclusivos
                self.functions_txt += self.build_input_function(input)

    def build_spawn(self):
        self.spawn_txt = ""
        self.spawn = self.actor.get("spawn")
        if self.spawn != None:
            if self.spawn.get("type") == "unique":
                self.update_txt += f"""
        if len(self.actor_list) == 0:
            actor = {self.class_name}(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
            self.actor_list.append(actor)
                """
            else:
                self.update_txt += f"""
        actor = {self.class_name}(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)))
        self.actor_list.append(actor)
                """

    def build_updates(self):
        self.update_txt = ""
        updates = self.actor.get("behaviors").get("updates")
        if updates != None:
            for update in updates:
                self.update_txt += f"""
        self.update_{update.get("action")}()
                """
                self.functions_txt += self.build_update_function(update) 


    def build_update_function(self,input):
        functions_txt = ""
        action = input.get("action")
        if action == "forward":
            functions_txt += f"""
    def update_{input.get("action")}(self):
        for actor in self.actor_list:
            actor.forward({input.get("param")})
            """

        elif action == "backward":
            functions_txt += f"""
    def update_{input.get("action")}(self):
        for actor in self.actor_list:
            actor.backward({input.get("param")})
            """

        elif action == "right":
            functions_txt += f"""
    def update_{input.get("action")}(self):
        for actor in self.actor_list:
            actor.right({input.get("param")})
            """

        elif action == "left":
            functions_txt += f"""
    def update_{input.get("action")}(self):
        for actor in self.actor_list:
            actor.left({input.get("param")})
            """
        elif action == "space_invader":
            functions_txt += f"""
    def update_{input.get("action")}(self):
        for actor in self.actor_list:
            actor.setheading(90)
            actor.forward(20)
            actor.setheading(270)
            actor.forward(30)
            actor.setheading(180)
            actor.forward(10)
            actor.setheading(90)
            """

        return functions_txt


    def build_input_function(self,input):
        functions_txt = ""
        action = input.get("action")

        if action == "forward":
            functions_txt += f"""
    def input_{input.get("key")}(self):
        for actor in self.actor_list:
            actor.forward({input.get("param")})
            """

        elif action == "backward":
            functions_txt += f"""
    def input_{input.get("key")}(self):
        for actor in self.actor_list:
            actor.backward({input.get("param")})
            """

        elif action == "right":
            functions_txt += f"""
    def input_{input.get("key")}(self):
        for actor in self.actor_list:
            actor.right({input.get("param")})
            """

        elif action == "left":
            functions_txt += f"""
    def input_{input.get("key")}(self):
        for actor in self.actor_list:
            actor.left({input.get("param")})
            """

        elif action == "strife_left":
            functions_txt += f"""
    def input_{input.get("key")}(self):
        for actor in self.actor_list:
            actor.setx(actor.xcor() - {input.get("param")})
            """
        elif action == "strife_right":
            functions_txt += f"""
    def input_{input.get("key")}(self):
        for actor in self.actor_list:
            actor.setx(actor.xcor() + {input.get("param")})
            """

        return functions_txt
    def build(self, actor):
        self.actor = actor
        self.class_name = str.title(self.actor.get("name"))
        self.functions_txt = ""
        self.build_inputs()
        self.build_updates()
        self.build_spawn()
        self.manager_txt = f"""
import random
from {self.actor.get("name")} import {self.class_name}

class {self.class_name}Manager():

    def __init__(self, screen):
        self.actor_list = []
        self.spawn_colors = {self.spawn.get("colors")}
        self.spawn_positions = {self.spawn.get("positions")}
        
        self.screen = screen
        
    def setup(self):
        pass

    def input(self):
        {self.input_txt}
        pass

    def update(self,start):
        {self.update_txt}
        pass
    
    {self.functions_txt}
    """
        self.manager_imports += f"""
    
from {self.actor.get("name")}_manager import {self.class_name}Manager"""

        self.manager_setups += f"""
        self.{self.actor.get("name")}_manager = {self.class_name}Manager(self.screen)"""
        self.input_setups += f"""
        self.{self.actor.get("name")}_manager.input()"""
        self.setup_setups += f"""
        self.{self.actor.get("name")}_manager.setup()"""
        self.update_setups += f"""
        self.{self.actor.get("name")}_manager.update(start)"""
        file = open(f"src/{self.actor.get('name')}_manager.py", "w")
        file.write(self.manager_txt)
        file.close()
        pass