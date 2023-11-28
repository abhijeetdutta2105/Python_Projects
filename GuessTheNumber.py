# a little bit about global variables
import random
'''
change_me = "Abhijeet" # global variable
print(f'Original global variable {change_me}')

# it is not possible to change global variable without using global keyword
def modify():
  global change_me
  change_me = "Kumar"

modify()
print(f'Modified global variable {change_me}')
'''
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


def guess_game():

  def play_game(num_guess, actual_number):
    if num_guess == 0:
      print('You have run out of guesses. You lose!')
      exit()

    user_num = int(input('Make a guess: '))

    if user_num == actual_number:
      print('You have guessed the correct number!')
      exit()

    elif user_num > actual_number:
      print('Too High')

    else:
      print('Too Low')

    print(f'You have {num_guess-1} attempts left to guess the correct one.')
    play_game(num_guess - 1, actual_number)

  print(logo)
  print('Welcome to Number Guessing Game!')
  print('I am thinking of a number between 1 to 100')

  actual_number = random.randint(1, 100)
  print(f'Psst, the number is {actual_number}')

  level = input('Enter the difficulty level - easy or hard: ').lower()

  if level == 'easy':
    print('You have 10 guesses to guess the number')
    play_game(EASY_LEVEL_TURNS, actual_number)

  elif level == 'hard':
    print('You have 5 guesses to guess the number')
    play_game(HARD_LEVEL_TURNS, actual_number)

  else:
    print('Invalid difficulty level')
    quit()
