# spell out the Alphabets using Dictionary Given : NATO Alphabet Project

import pandas

alphabet_data = pandas.read_csv('nato_phonetic_alphabet.csv')

# alphabet_dict = {letter : code for (letter,code) in zip(alphabet_data['letter'].to_list(),alphabet_data['code'].to_list())}

alphabet_dict = {row[1].letter : row[1].code for row in alphabet_data.iterrows()}
# in above row[0] corresponds to the index and row[1] corresponds to the actual Series for our Dataframe

# ask for the word
word = input('Enter the word : ').upper()
print([alphabet_dict[letter] for letter in word])

