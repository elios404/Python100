from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_table = Menu()
coffee_mac = CoffeeMaker()
money_mac = MoneyMachine()

while(True):
    # 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):​ "
    order = input(f"What would you like? {menu_table.get_items()}:").lower()
    
    # 2. Turn off the Coffee Machine by entering “off​ ” to the prompt. 
    if order == "off":
        print("Enjoy ur day!! Machine turns off")
        break
    # 3. Print report. 
    elif order == "report":
        coffee_mac.report()
        money_mac.report()
    else:
        # 4. Check resources sufficient? 
        user_coffee = menu_table.find_drink(order)
        if user_coffee != None: #if user_coffee is in Menu
            if coffee_mac.is_resource_sufficient(user_coffee):
                # 5. 5. Process coins.
                # 6. Check transaction successful?
                if money_mac.make_payment(user_coffee.cost):
                    # 7. Make Coffee.
                    coffee_mac.make_coffee(user_coffee)
        else:
            print(f"There are no menu of '{order}'! Try again.")