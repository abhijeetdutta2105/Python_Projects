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
quarter, dime, nickle, penny = 0, 0, 0, 0


def ask_for_coins():
  global quarter, dime, nickle, penny
  quarter = int(input('how many quarters?: '))
  dime = int(input('how many dimes?: '))
  nickle = int(input('how many nickles?: '))
  penny = int(input('how many pennies?: '))


def reset():
  global quarter, dime, nickle, penny
  quarter = dime = nickle = penny = 0


def compute_change(quarter, dime, nickle, penny, amount):
  global money
  cost = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
  change = round(cost - amount, 2)
  if change < 0:
      print("Sorry that's not enough money. Money refunded")
  else:
      print(f"Here is ${change} in change.")
      money += amount
      print(f"Here is your {choice} ☕. Enjoy!")
      update_resource(choice)
  reset()


def get_amount(choice):
  return MENU[choice]['cost']


def resource_sufficient(choice):
  water, coffee, milk = resources['water'], resources['coffee'], resources['milk']
  required_water = MENU[choice]['ingredients']['water']
  required_coffee = MENU[choice]['ingredients']['coffee']
  required_milk = 0

  if choice != 'espresso':
      required_milk = MENU[choice]['ingredients']['milk']

  if choice == 'espresso':
      return required_water <= water and required_coffee <= coffee

  return required_milk <= milk and required_coffee <= coffee and required_water <= water


def find_deficient(choice):
  if MENU[choice]['ingredients']['water'] > resources['water']:
      return 'water'
  elif MENU[choice]['ingredients']['coffee'] > resources['coffee']:
      return 'coffee'
  return 'milk'


def update_resource(choice):
  resources['water'] -= MENU[choice]['ingredients']['water']
  resources['coffee'] -= MENU[choice]['ingredients']['coffee']

  if choice != 'espresso':
      resources['milk'] -= MENU[choice]['ingredients']['milk']


def get_report():
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: {money}$")


choice = ''
while True:
  choice = input('What would you like? (espresso/latte/cappuccino/report/exit): ').lower()
  if choice == 'exit':
      exit()

  elif choice == 'report':
      get_report()
      continue

  elif choice in ['espresso', 'latte', 'cappuccino']:

      if resource_sufficient(choice):
          print("Please insert coins")
          ask_for_coins()
          compute_change(quarter, dime, nickle, penny, get_amount(choice))

      else:
          print(f"Sorry there is not enough {find_deficient(choice)}")

  else:
      print('Please enter a valid choice')
