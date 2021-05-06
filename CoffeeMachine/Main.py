import CoffeMachine

userSelection = input("What would you like? (espresso/latte/cappuccino):")

water = CoffeMachine.resources['water']
milk = CoffeMachine.resources['milk']
coffee = CoffeMachine.resources['coffee']
money = 0

is_on = True
def generatereport():
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee} \nMoney: {money}")

def checkresources(selection):
    selectionwater = CoffeMachine.MENU[selection]['ingredients']['water']
    #if CoffeMachine.resources['']

while is_on:
    if userSelection == "off":
        print("Shutting Down...")
        is_on = False
    elif userSelection == "report":
        print("Generating Report...")
        generatereport()
        is_on = False
    elif userSelection == "espresso":
        checkresources(userSelection)
        print()
        is_on = False
    elif userSelection == "latte":
        checkresources(userSelection)
        print()
        is_on = False
    elif userSelection == "cappuccino":
        checkresources(userSelection)
        print()
        is_on = False
