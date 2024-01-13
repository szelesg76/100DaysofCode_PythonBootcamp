from os import system
from coffe_machine_menu import MENU


#from data.coffe_machine_resouce_t import MENU as menu

system('clear')


def report(resources: dict, money: int):
    for key, value in resources.items():
        if key == 'water' or key == 'milk':
            print(f"{key}: {value}ml")
        else:
            print(f"{key}: {value}g")
    print(f"Money: ${money}")  

def check_resources(needs: str, resources: dict, MENU: dict):
    missing_ingredients = set()
    for ingredients_key, ingredients_value in MENU[needs]['ingredients'].items():
        if resources[ingredients_key]-ingredients_value < 0:
            missing_ingredients.add(ingredients_key)       
    if len(missing_ingredients) > 0:
        return missing_ingredients
    else:
        return True
    
def decrease_resources(needs: str, resources: dict, MENU: dict):
    for ingredients_key, ingredients_value in MENU[needs]['ingredients'].items():
        resources[ingredients_key] = resources[ingredients_key]-ingredients_value


coins = ('quarters','dimes','nickles','pennies')
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_money(coins: tuple) -> int:
    return_value = 0
    for coin in coins:
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

        
def caffe_making(coffe_type: str, profit: float):
    status = check_resources(coffe_type, resources, MENU)
    if status != True:
        print(f"Sorry, there is not enough {status}.")
    elif status == True:
        money_in = float(get_money(coins))
        cost = float(MENU[coffe_type]['cost'])
        if  cost> money_in:
            print(f"Sorry that's not enough money. Money refunded.")
        elif cost < money_in:                
            print(f"Here is ${money_in-cost} dollars in change.")
            decrease_resources(coffe_type, resources, MENU)
            print(f"Here is your {coffe_type}. ☕ Enjoy!")
            profit += cost
        elif cost == money_in:
            decrease_resources(coffe_type, resources, MENU)
            print(f"Here is your {coffe_type}. ☕ Enjoy!")
            profit += cost
    return profit

while True:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == 'report':
        report(resources, profit)
    elif choose == 'off':
        break
    elif choose == 'espresso':
        profit = caffe_making('espresso',profit)
    elif choose == 'latte':
        profit = caffe_making('latte',profit)
    elif choose == 'cappucino':
        profit = caffe_making('cappucino',profit)