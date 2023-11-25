import random


def generate_password():
  print('Welcome to PyPassword Generator!')

  letter_length = int(
      input('How many letters would you like in your password?\n'))

  symbol_length = int(
      input('How many symbol would you like in your password?\n'))

  number_length = int(
      input('How many numbers would you like in your password?\n'))

  letters = 'abcdefghijklmnopqrstuvwxyz'
  numbers = '012346789'
  symbols = '!@#$%^&*()_+-=[]{}|;:,.<>/?'

  # Easy Level: your letters, symbols and numbers occur in sequential order

  if letter_length < 0 or symbol_length < 0 or number_length < 0:
    print('Please enter a positive number for the inputs.')
    quit()

  password = ''

  if letter_length > 0:
    for count in range(letter_length):
      password += random.choice(letters)

  if symbol_length > 0:
    for count in range(symbol_length):
      password += random.choice(symbols)

  if number_length > 0:
    for count in range(number_length):
      password += random.choice(numbers)

  print('Your sequential password is: ', password)

  # Difficult Level: your characters occur in random order

  password_list = list(password)
  random.shuffle(password_list)  # this is used to shuffle the list
  password = ''.join(password_list)
  print('Your random password is: ', password)


generate_password()
