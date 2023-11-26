# A type of encripytion method that shifts the letters of the alphabet by a certain amount.


def perform_cipher():
  logo = """           
   ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
  a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
  8b         ,adPPPPP88 8PP""" """"  `"Y8ba,  ,adPPPPP88 88          
  "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
   `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
              88             88                                 
             ""             88                                 
                            88                                 
   ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
  a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
  8b         88 88       d8 88       88 8PP""" """" 88          
  "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
   `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                88                                             
                88           
  """

  def encrypt(text, shift):
    answer = ''
    if shift < 0:
      return 'Wrong shift value!'
    elif shift == 0:
      return text

    else:
      shift %= 26 # to handle numbers that are greater than 26
      for char in text:
        if char.isalpha():
          if ord(char) + shift <= ord('z'):
            new_char = chr(ord(char) + shift)
            answer += new_char
          else:
            diff = ord('z') - ord(char)
            new_char = chr(ord('a') + shift - diff - 1)
            answer += new_char
        else:
          answer += char
      
      return answer

  def decrypt(text, shift):
    answer = ''
    if shift < 0:
      return 'Wrong shift value!'
    elif shift == 0:
      return text

    else:
      shift %= 26 # to handle numbers that are greater than 26
      for char in text:
        if char.isalpha():
          if ord(char) - shift >= ord('a'):
            new_char = chr(ord(char) - shift)
            answer += new_char
          else:
            diff = ord(char) - ord('a')
            new_char = chr(ord('z') - (shift - diff - 1))
            answer += new_char

        else:
          answer += char
          
      return answer

  def ask_input(choice):
    if choice == 'no':
      print('Thank You for using our Caesar Cipher!')
      exit()
    option = input(
        'Type "encode" to encode a message, or "decode" to decode a message.\n')
    while option != 'encode' and option !='decode':
      print('Please type "encode" or "decode".')
      option = input(
        'Type "encode" to encode a message, or "decode" to decode a message.\n')
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    result = encrypt(text, shift) if option == 'encode' else decrypt(text, shift)
    

    print(f'Here is the encoded result : {result}')
    choice = input('Would you like to continue? (yes/no)\n')
    ask_input(choice)

  print(logo)
  choice = 'yes'
  ask_input(choice)
