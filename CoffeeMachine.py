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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

def is_res_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def order(require):
    global money
    if require == "report":
        for item in resources:
                print(f"{item.capitalize()}: {resources[item]}")

    else:
        items = MENU[require]["ingredients"]
        item_money = MENU[require]["cost"]

        if is_res_sufficient(items):
            print("Please insert a coin.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            quarters *= 0.25
            dimes *= 0.1
            nickles *= 0.05
            pennies *= 0.01
            input_money = quarters + dimes + nickles + pennies

            if input_money < item_money :
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = input_money - item_money
                for item in items:
                    resources[item] -= items[item]
                money += item_money
                print(f"Here is ${change} in change.")
                print(f"Here is your {require}. Enjoy!")

while True:
    require = input("  What would you like? (espresso/latte/cappuccino): ")
    if require == "off":
        break
    else:
        order(require)
        continue