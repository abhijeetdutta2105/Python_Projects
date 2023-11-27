# from replit import clear (it is replit platform specific function)

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def perform_auction():

  print(logo)
  print('Welcome to the secret auction program.')

  def put_bid(choice,bidder_info,winner):
    if(choice == 'no'):
      print(f'The winner is {winner} with a bid of ${bidder_info[winner]}.')
      exit()

    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    bidder_info[name] = bid

    if bid > bidder_info[winner]:
      winner = name

    choice = input('Are there anymore bidders? Type "yes" or "no". ').lower()
    # clear() under the replit platform
    put_bid(choice,bidder_info,winner)

  winner = ''
  bidder_info = {'':-1}
  put_bid('yes',bidder_info,winner)