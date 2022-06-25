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
    "money": 0.0,
}


def resource_calculation(original_resources, coffee_resources):
    """This function checks if all the resources are enough to make a coffee and returns True.
        If insufficient, it returns False"""
    for item in coffee_resources:
        if coffee_resources[item] > original_resources[item]:
            print(f"Sorry there's not enough {item}.")
            return False
        else:
            return True


def transaction_successful():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_amount_inserted = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if total_amount_inserted >= MENU[user_input]["cost"]:
        remaining_amount = total_amount_inserted - MENU[user_input]["cost"]
        remaining_amount = "{:.2f}".format(remaining_amount)
        print(f"Here's ${remaining_amount} change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def resource_deduction(original_resources, coffee_resources):
    """This function deducts drink resources from main resources after making a drink.
        It will also add to the profits the cost of coffee."""
    for item in coffee_resources:
        original_resources[item] -= coffee_resources[item]
    original_resources["money"] += MENU[user_input]["cost"]


continue_serving = True
while continue_serving:
    user_input = input("What would you like? (espresso/latte/cappuccino):  ").lower()

    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    elif user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
        resources_left = resource_calculation(resources, MENU[user_input]["ingredients"])
        if resources_left:  # It's the same way of saying If resources_left == True:
            if transaction_successful():
                resource_deduction(resources, MENU[user_input]["ingredients"])
                print(f"Here's your {user_input}. ☕ Enjoy\n")

    elif user_input == "off":
        continue_serving = False
