from Menu import Menu
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine
def customer_order():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:

        order = input(f"What would you like? ({menu.get_items()})")
        if order =="off":
            print("Machine shutted down")
            break
        elif order=="report":
            coffee_maker.show_report()
            continue
        elif order == "money":
            money_machine.report()
            continue

        else:

            drink = menu.find_drink(order)
            drink_ingredients = drink.ingredients
            drink_cost = drink.cost

            enough_resources = coffee_maker.check_resources(drink_ingredients)
            if enough_resources:
                enough_money = money_machine.check_money(drink_cost)
                if enough_money:
                    coffee_maker.make_coffee(drink_ingredients)
                    print(f"Here is your {order}. Enjoy!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    customer_order()




