class RuleBuilder:

    def __init__(self, rules):
        self.rules_setups = ""
        self.rules = rules

    def build(self):
        for rule in self.rules:
            print(rule)
            if rule.get("trigger") == "collision":
                self.rules_setups += f"""
        if self.{rule.get("actor1")}_manager.check_collision(self.{rule.get("actor2")}_manager.actor_list):
        """
            if rule.get("consequence") == "print":
                self.rules_setups += f"""
            print("ALOU")
        """
            print(self.rules_setups)
