from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
machine = MoneyMachine()
menu_item = Menu()
choice = ''

while True:
    options = menu_item.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()

    if choice == 'exit':
        exit()
    elif choice == 'report':
        maker.report()
        machine.report()
    elif choice in ['espresso', 'latte', 'cappuccino']:
        drink = menu_item.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                maker.make_coffee(drink)
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print('Please enter a valid choice')



