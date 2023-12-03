# Exploring prettytable module: A simple Python
# library for easily displaying tabular data in a visually appealing ASCII table format

from prettytable import PrettyTable

table = PrettyTable()

# you want to add data column by column

# you change the alignment by table.align = 'c' or 'l' or 'r' for centre, left or right
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])

table.add_column("Type", ['Electric', 'Water', 'Fire'])

print(table)
