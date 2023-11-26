# Hangman - a game where user has to guess a word and if fails then a little man would die

# from replit import clear
# this is a replit function that clears the screen

def play_hangman():
  import random
  
  import Hangman_art
  import Hangman_words
  
  word_list = Hangman_words.word_list
  
  chosen_word = random.choice(word_list)
  
  stages = Hangman_art.stages
  lives = 6
  # testing code
  print(Hangman_art.logo)
  print(f'Psst, the solution is {chosen_word}.')
  
  display = list('-' * len(chosen_word))
  
  while '-' in display and lives > 0:
    guess = input("Guess a letter: ").lower()
  
    #clear() under the replit in-built functions
    if guess in display:
      print(f"You've already guessed {guess}.")
      continue
  
    for idx in range(len(chosen_word)):
      if chosen_word[idx] == guess:
        display[idx] = guess
  
    if guess not in chosen_word:
      print(f'You chose {guess}, that is not in the word, you lose life')
      print(stages[lives - 1])
      lives -= 1
  
    print(display)
  
  if lives == 0:
    print('You Lose')
  
  else:
    print('You Win')
  