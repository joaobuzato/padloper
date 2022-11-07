

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
        self.padscreen.get_screen_obj().onkeyrelease(key='{input.get('key')}', fun=self.func_{input.get('action')})"""
                # TODO fazer inputs mais inclusivos
                self.functions_txt += self.build_function(input)

    def build_spawn(self):
        self.spawn_txt = ""
        self.spawn = self.actor.get("spawn")
        if self.spawn != None:
            if self.spawn.get("type") == "unique":
                self.update_txt += f"""
        if len(self.actor_list) == 0:
            actor = {self.class_name}(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)), padscreen=self.padscreen)
            self.actor_list.append(actor)
                """
            else:
                self.update_txt += f"""
        if len(self.actor_list) < {self.spawn.get("max_num")}:
            actor = {self.class_name}(color=random.choice(self.spawn_colors), position=(random.choice(self.spawn_positions)), padscreen=self.padscreen)
            self.actor_list.append(actor)
            print(len(self.actor_list))
                """

    def build_updates(self):
        self.update_txt = ""
        updates = self.actor.get("behaviors").get("updates")
        if updates != None:
            for update in updates:
                self.update_txt += f"""
        self.func_{update.get("action")}()
                """
                self.functions_txt += self.build_function(update) 


    def build_function(self,input):
        functions_txt = f"""
    def func_{input.get("action")}(self):
        for actor in self.actor_list:
            if actor.is_out_of_screen():
                self.remove_actor(actor)
        """
        action = input.get("action")
        if action == "forward":
            functions_txt += f"""
            actor.forward({input.get("param")})
            """
        elif action == "backward":
            functions_txt += f"""
            actor.backward({input.get("param")})
            """
        elif action == "right":
            functions_txt += f"""
            actor.right({input.get("param")})
            """
        elif action == "left":
            functions_txt += f"""
            actor.left({input.get("param")})
            """
        elif action == "strife_left":
            functions_txt += f"""
            actor.setx(actor.xcor() - {input.get("param")})
            """
        elif action == "strife_right":
            functions_txt += f"""
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

    def __init__(self, padscreen):
        self.actor_list = []
        self.spawn_colors = {self.spawn.get("colors")}
        self.spawn_positions = {self.spawn.get("positions")}
        
        self.padscreen = padscreen

    def remove_actor(self,actor):
        actor.goto(10000,10000)
        self.actor_list.remove(actor)
        """
        self.manager_txt +="""
    def check_collision(self, object_list):
        collision = {"has_collision" : False}
        for actor in self.actor_list:
            for obj in object_list:
                if actor.touches(obj):
                    collision = {
                        "has_collision": True,
                        "actor1" : actor,
                        "actor2" : obj
                    }
                    return collision
                    
        return collision

    def check_position(self, **kwargs):
        x_pos = kwargs.get("x_pos")
        y_pos = kwargs.get("y_pos")
        x_cond = kwargs.get("x_cond")
        y_cond = kwargs.get("y_cond")
        for actor in self.actor_list:
            if x_pos is None:
                if actor.check_y_position(y_pos,y_cond):
                    return { "position_checked" : True, "actor" : actor}
            elif y_pos is None:
                if actor.check_x_position(x_pos,x_cond):
                    return { "position_checked" : True, "actor" : actor}
            else:
                if actor.check_y_position(y_pos, y_cond) and actor.check_x_position(x_pos, x_cond):
                    return { "position_checked" : True, "actor" : actor}

        return { "position_checked" : False }
        
        """

        
        self.manager_txt += f"""
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
        self.{self.actor.get("name")}_manager = {self.class_name}Manager(self.padscreen)"""
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