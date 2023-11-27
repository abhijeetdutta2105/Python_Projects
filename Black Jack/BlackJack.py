import random

from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def play_game(option):
  if option == "no":
    print("Thanks for trying our game.")
    exit()

  print(logo)
  # cards has 2-10 then Ace, King, Queen, Jack
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
  is_game_over = False
  def deal_card(cards):
    """returns a random card from the deck"""
    return random.choice(cards)

  def calculate_score(card_collection):
    """takes the card_collection and calculates total score based on some rules"""
    if sum(card_collection) == 21 and len(card_collection) == 2:
      return 0 # this represents a blackjack

    elif sum(card_collection) > 21 and 11 in card_collection:
      card_collection.remove(11)
      card_collection.append(1)
    return sum(card_collection)

  def compare(user_score, computer_score):
    if user_score == computer_score:
      return "Draw 🙃"
    elif computer_score == 0:
      return "Lose! Opponent has the BlackJack 🥶"
    elif user_score == 0:
      return "Win! You have the BlackJack 😎"
    elif user_score > 21:
      return "You went Over! You lose 😨"
    elif computer_score > 21:
      return "Computer went Over! You win 😍"
    elif user_score > computer_score:
      return "You Win because you have more 😏"
    else:
      return "You Lose because you have less points 😥"


  computer = [deal_card(cards),deal_card(cards)]
  user = [deal_card(cards),deal_card(cards)]
  user_score = calculate_score(user)
  computer_score = calculate_score(computer)
  while not is_game_over:

    choice = 'yes'
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
      print('Game Ends!')

    else:
      choice = input('Do you want to draw another card then say "yes" or "no" to pass: ').lower()
      if choice == 'yes':
        user.append(deal_card(cards))

      else:
        is_game_over = True

  while computer_score!=0 and computer_score < 17:
    computer.append(deal_card(cards))
    computer_score = calculate_score(computer)

  print(f'Your final hand: {user}, your final score: {user_score}')
  print(f'Computer\'s final hand: {computer}, computer\'s final score: {computer_score}')
  print(compare(user_score,computer_score))

  option = input("Do you want to play another game? Type 'yes' or 'no': ").lower()
  clear()
  play_game(option)




