"""This is a docstring which describes the module"""
from os import system
from coffe_machine_menu import MENU
system('clear')


def report(resources: dict, money: int):
    """_summary_

    Args:
        resources (dict): _description_
        money (int): _description_
    """
    for key, value in resources.items():
        if key == 'water' or key == 'milk':
            print(f"{key}: {value}ml")
        else:
            print(f"{key}: {value}g")
    print(f"Money: ${money}")

def check_resources(needs: str, resources: dict, menu: dict):
    """_summary_

    Args:
        needs (str): _description_
        resources (dict): _description_
        menu (dict): _description_

    Returns:
        _type_: _description_
    """
    missing_ingredients = set()
    for ingredients_key, ingredients_value in menu[needs]['ingredients'].items():
        if resources[ingredients_key]-ingredients_value < 0:
            missing_ingredients.add(ingredients_key)
    if len(missing_ingredients) > 0:
        return missing_ingredients
    return True

def decrease_resources(needs: str, resources: dict, menu: dict):
    """_summary_

    Args:
        needs (str): _description_
        resources (dict): _description_
        menu (dict): _description_
    """
    for ingredients_key, ingredients_value in menu[needs]['ingredients'].items():
        resources[ingredients_key] = resources[ingredients_key]-ingredients_value


coins = ('quarters','dimes','nickles','pennies')
PROFIT = 0
coffe_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_money(in_coins: tuple) -> int:
    """Get and count the money

    Args:
        coins (tuple): Coin types

    Returns:
        int: Sum of the money
    """
    return_value = 0
    for coin in in_coins:
        value = int(input(f"how many {coin}: "))
        if coin == 'quarters' and value > 0:
            return_value += value * 0.25
        elif coin == 'dimes' and value > 0:
            return_value += value * 0.10
        elif coin == 'nickles' and value > 0:
            return_value += value * 0.05
        elif coin == 'pennies' and value > 0:
            return_value += value * 0.01
    return format(return_value, '.2f')


def caffe_making(coffe_type: str, profit: float) -> float:
    """_summary_

    Args:
        coffe_type (str): _description_
        profit (float): _description_

    Returns:
        _type_: _description_
    """
    status = check_resources(coffe_type, coffe_resources, MENU)
    if not status:
        print(f"Sorry, there is not enough {status}.")
    elif status:
        money_in = round(float(get_money(coins)),2)
        cost = float(MENU[coffe_type]['cost'])
        if  cost> money_in:
            print("Sorry that's not enough money. Money refunded.")
        elif cost < money_in:
            print(f"Here is ${money_in-cost} dollars in change.")
            decrease_resources(coffe_type, coffe_resources, MENU)
            print(f"Here is your {coffe_type}. ☕ Enjoy!")
            profit += cost
        elif cost == money_in:
            decrease_resources(coffe_type, coffe_resources, MENU)
            print(f"Here is your {coffe_type}. ☕ Enjoy!")
            profit += cost
    return profit

while True:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == 'report':
        report(coffe_resources, PROFIT)
    elif choose == 'off':
        break
    elif choose == 'espresso':
        PROFIT = caffe_making('espresso',PROFIT)
    elif choose == 'latte':
        PROFIT = caffe_making('latte',PROFIT)
    elif choose == 'cappucino':
        PROFIT = caffe_making('cappucino',PROFIT)
