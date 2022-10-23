
from enemy import Enemy

class EnemyManager():

    def __init__(self, screen):
        self.actor_list = []
        
        self.screen = screen
        
    def setup(self):
        actor = Enemy()
        self.actor_list.append(actor)

    def input(self):
        
        pass

    def update(self):
        
        self.update_space_invader()
                
        pass
    
    
    def update_space_invader(self):
        for actor in self.actor_list:
            actor.setheading(90)
            actor.forward(20)
            actor.setheading(270)
            actor.forward(30)
            actor.setheading(180)
            actor.forward(10)
            actor.setheading(90)
            
    