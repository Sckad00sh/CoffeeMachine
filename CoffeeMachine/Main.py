import CoffeMachine

userSelection = input("What would you like? (espresso/latte/cappuccino):")

water = CoffeMachine.resources['water']
milk = CoffeMachine.resources['milk']
coffee = CoffeMachine.resources['coffee']
money = CoffeMachine.resources['money']

is_on = True


def generatereport():
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")


def check_resources(ingredients):
    # Todo: 1. get ingredients for selection
    for item in ingredients:
        if ingredients[item] >= CoffeMachine.resources[item]:
            print(f'Not enough {item}')
            return False
    return True

def process_coins(cost):
    print (f'Insert ${cost}')
    quarters = input('Insert quarters: ')
    dimes = input('Insert dimes: ')
    nickles = input('Insert nickles: ')
    pennies = input('Insert pennies: ')

    total = (0.25 * float(quarters)) + (0.10 * float(dimes)) + (0.05 * float(nickles)) + (0.01 * float(pennies))
    money == money + total

    if total == cost:
        return True
    if total > cost:
        print(f'Total Inserted ${total}')
        print('Dispensing change')
        change = total - cost
        print(f'Your change is ${change}')
        money == money - change
        return True
    else:
        print(f'Sorry that\'s not enough money. Money refunded')
        return False


while is_on:
    if userSelection == "off":
        print("Shutting Down...")
        is_on = False
    elif userSelection == "report":
        print("Generating Report...")
        generatereport()
        is_on = False
    else:
        choice = CoffeMachine.MENU[userSelection]
        if check_resources(choice['ingredients']):
            process_coins(choice['cost'])
        generatereport()
        is_on = False
