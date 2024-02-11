class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def show_report(self):
        for r in self.resources:
            print(f" {r} : {self.resources[r]}")
    def check_resources(self,drink_ingredients):
        for ingredient in drink_ingredients:
            if drink_ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True

    def make_coffee(self,drink_ingredients):
        for ingredient in drink_ingredients:
            self.resources[ingredient] -= drink_ingredients[ingredient]