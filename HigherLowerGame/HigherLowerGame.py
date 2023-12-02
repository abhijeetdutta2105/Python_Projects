import HigherLowerGameData

import random

def play_game():
  logo = """
      __  ___       __             
     / / / (_)___ _/ /_  ___  _____
    / /_/ / / __ `/ __ \/ _ \/ ___/
   / __  / / /_/ / / / /  __/ /    
  /_/ ///_/\__, /_/ /_/\___/_/     
     / /  /____/_      _____  _____
    / /   / __ \ | /| / / _ \/ ___/
   / /___/ /_/ / |/ |/ /  __/ /    
  /_____/\____/|__/|__/\___/_/     
  """
  
  vs = """
   _    __    
  | |  / /____
  | | / / ___/
  | |/ (__  ) 
  |___/____(_)
  """
  
  print(logo)

  data = HigherLowerGameData.data
  
  result = 'correct'
  score = 0
  data1 = random.choice(data)
  data.remove(data1)
  
  def compare(data1, data2):
    return 'A' if data1['follower_count'] >= data2['follower_count'] else 'B'
  
  while result == 'correct' and len(data) > 1:
  
    data2 = random.choice(data)
    data.remove(data2)
  
    print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}")
  
    print(vs)
  
    print(f"Compare B: {data2['name']}, a {data2['description']}, from {data2['country']}")
  
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  
    if guess == compare(data1,data2):
      score += 1
      print(f"You're right! Current score: {score}")
      result = 'correct'
      if guess == 'A':
        data.append(data1)
  
      else:
        data.append(data2)
        data1 = data2
    else:
      result = 'incorrect'
      print(f"Sorry, that's wrong. Final score: {score}")