
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
        
        self.update_forward()
                
        self.update_right()
                
        pass
    
    
    def update_forward(self):
        for actor in self.actor_list:
            actor.forward(10)
            
    def update_right(self):
        for actor in self.actor_list:
            actor.right(10)
            
    