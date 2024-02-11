class MoneyMachine:
    COINS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def insert_coins(self):
        print("Please insert some coins!")

        for c in self.COINS:
            self.money_received += int(input(f"How many {c}: ")) * self.COINS[c]

        print(f"You Inserted {self.money_received} dollars")
        return self.money_received

    def check_money(self, drink_cost):
        self.insert_coins()
        if self.money_received < drink_cost:
            print("Sorry that's not enough money. Money refunded")
            return False
        elif self.money_received > drink_cost:
            self.profit += drink_cost
            change = str(round(self.money_received - drink_cost, 2))
            self.money_received = 0
            print(f"Here is ${change} dollars in change.")
            return True
        else:
            self.profit += drink_cost
            self.money_received = 0
            return True
    def report(self):
        print(f"Money report: ${self.profit}")