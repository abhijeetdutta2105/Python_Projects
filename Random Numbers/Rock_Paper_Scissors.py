# Rock Paper Scissors Game using Random Module and Ascii Art

import random

user_choice = input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\

'''

paper = '''

 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|          
'''

scissor = '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/

'''

if user_choice == '0':
  print(rock)
elif user_choice == '1':
  print(paper)
else:
  print(scissor)

computer_choice = random.randint(0, 2)

print('Computer chose:')
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissor)

if (int(user_choice) == computer_choice):
  print('Tie')

elif user_choice == '0' and computer_choice == 1:
  print('You lose')

elif user_choice == '0' and computer_choice == 2:
  print('You win')

elif user_choice == '1' and computer_choice == 0:
  print('You win')

elif user_choice == '1' and computer_choice == 2:
  print('You lose')

elif user_choice == '2' and computer_choice == 0:
  print('You lose')

elif user_choice == '2' and computer_choice == 1:
  print('You win')
