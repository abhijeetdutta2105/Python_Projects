import pandas

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# you can get the list of column headers using list(dataframe)
# print(list(squirrel_data))

color_fur = squirrel_data['Primary Fur Color']
squirrel_dict = {}
for color in color_fur:
    if color in squirrel_dict:
        squirrel_dict[color]+=1
    else:
        squirrel_dict[color] = 1

to_remove = list(squirrel_dict.keys())[0]
squirrel_dict.pop(to_remove)
# print(squirrel_dict)

squirrel_count_dict = {
    "Fur Color" : list(squirrel_dict.keys()),
    "Count" : list(squirrel_dict.values())
}
# print(squirrel_count_dict)
squirrel_count = pandas.DataFrame(squirrel_count_dict)

squirrel_count.to_csv('squirrel_count.csv')

