class RuleBuilder:

    def __init__(self, rules):
        self.rules_setups = ""
        self.rules = rules

    def build(self):
        for rule in self.rules:
            if rule.get("trigger") == "collision":
                self.rules_setups += f"""
        if self.{rule.get("actor1")}_manager.check_collision(self.{rule.get("actor2")}_manager.actor_list):
        """
            if rule.get("consequence") == "print":
                self.rules_setups += f"""
            print("collision!")
        """
            elif rule.get("consequence") == "point":
                self.rules_setups += f"""
            self.scoreboard.point()    
        """
            elif rule.get("consequence") == "gameover":
                self.rules_setups += f"""
            self.scoreboard.game_over()
            self.game_is_on = False
        """
