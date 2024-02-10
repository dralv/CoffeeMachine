MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
    "money": 0
}
def show_report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")

def client_order():
    machine_on = True
    while machine_on:
        order = input("What would you like? (espresso/latte/cappuccino)")
        if order =="off":
            machine_on = False
            break
        elif order=="report":
            print_report()
            continue
        else:
            drink = MENU[order]
            drink_ingredients = drink["ingredients"]
            drink_cost = drink["cost"]
            enough_resources = check_resources(drink_ingredients)
            if enough_resources:
                customer_money = insert_coins()
                enough_money = check_money(customer_money,drink_cost)
                if enough_money:
                    make_coffe(drink_ingredients)
                    print(f"Here is your {order}. Enjoy!")
def insert_coins():
    print("Please insert some coins!")
    quarters = int(input("Insert quarters"))

    dimes = int(input("Insert dimes"))

    nickels = int(input("Insert nickels"))

    pennies = int(input("Insert pennies"))

    dollars = (quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)

    print(f"You Inserted {dollars} dollars")
    return dollars

def check_resources(drink_ingredients):
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def check_money(customer_money,drink_cost):
    if customer_money < drink_cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif customer_money > drink_cost:
        resources["money"] += drink_cost
        change = str(round(customer_money - drink_cost, 2))
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        resources["money"] += drink_cost
        return True
def make_coffe(drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
def print_report():
    for i in resources:
        print(f"{i} : {resources[i]}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client_order()
    print("Machine shutted down")



