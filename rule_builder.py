class RuleBuilder:

    def __init__(self, rules):
        self.rules_setups = ""
        self.rules = rules

    def build(self):
        for rule in self.rules:
            if rule.get("trigger") == "collision":
                self.rules_setups += f"""
        obj = self.{rule.get("actor1")}_manager.check_collision(self.{rule.get("actor2")}_manager.actor_list)
        if obj.get('has_collision'):
        """
            if rule.get("trigger") == "position" :
                x_pos = None
                x_cond = None
                y_pos = None
                y_cond = None
                if rule.get("x_pos") != "":
                    x_pos = rule.get("x_pos")
                    x_cond = rule.get("x_cond")
                if rule.get("y_pos") != "":
                    y_pos = rule.get("y_pos")
                    y_cond = rule.get("y_cond")
                
                self.rules_setups += f"""
        obj = self.{rule.get("actor1")}_manager.check_position(y_pos={y_pos},x_pos={x_pos}, y_cond='{y_cond}',x_cond='{x_cond}')
        if obj.get("position_checked"):
                """
            
            if rule.get("trigger") == "score" :
                win_score = rule.get("win_score")
                self.rules_setups += f"""
        if self.scoreboard.score >= {win_score} :    
                """


            for consequence in rule.get('consequences'):
                if consequence.get("name") == "remove_actor":
                    self.rules_setups += f"""
                self.{rule.get("actor2")}_manager.remove_actor(obj.get("actor2"))
                """
                elif consequence.get("name") == "set_heading":
                    self.rules_setups += f"""
                obj.get("actor1").setheading({consequence.get("heading")})
                    """
                elif consequence.get("name") == "bounce_x" :
                    self.rules_setups += f"""
                obj.get("actor1").bounce_x()
                    """
                elif consequence.get("name") == "bounce_y" :
                    self.rules_setups += f"""
                obj.get("actor1").bounce_y()
                    """
                
                elif consequence.get("name") == "game_won":
                    self.rules_setups += f"""
                self.scoreboard.game_won()
                self.game_is_on = False
                """
                elif consequence.get("name") == "point":
                    self.rules_setups += f"""
                self.scoreboard.point()  
                """
                elif consequence.get("name") == "game_over":
                    self.rules_setups += f"""
                self.scoreboard.game_over()
                self.game_is_on = False
                """
                elif consequence.get("name") == "move_to":
                    self.rules_setups += f"""
                obj.get("actor1").goto({consequence.get("x"), consequence.get("y")})
                """
                else:
                    self.rules_setups += f"""
                pass
                """
