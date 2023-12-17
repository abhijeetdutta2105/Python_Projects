# there are 2 primary data structures of pandas: Series(1-D) and DataFrame(2-D)
import pandas

data = pandas.read_csv('weather_data.csv')

# print(type(data)) # DataFrame data structure
# print(type(data['temp'])) # Series data structure

# to_dict() method of DataFrame takes each column and entries a key(column_heading) and value(column) to the dictionary
data_dict = data.to_dict()
# print(data_dict)

# similarly to_list() of Series takes a column and entries a list item
day_list = data['day'].to_list()
# print(day_list)

# find the average temp using these functions
# temp_list = data['temp'].tolist()
# print(f'Average temperature of the week : {sum(temp_list)/len(temp_list)}')

# We will use Series functions to do our job for computing the average
print('Average temperature of the week',data['temp'].mean())

print('Maximum temperature',data['temp'].max())

# alt way of getting column is to just call data.column_name
# print(data.condition)

# Get rows of our DataFrame
print(data[data.day == 'Wednesday'])

# Get row where the temperature was maximum
max_temp = data['temp'].max()

print(data[data.temp == max_temp])

# max_temp in Fahrenheit
# use the formula (9/5)*c + 32
print('***********')

# create a dataframe from scratch
student_dict = {
    "students" : ["Amy","James","Angela"],
    "scores" : [76,56,65]
}

student_data = pandas.DataFrame(student_dict)
print(student_data)
# you can even convert the above dataframe to csv using to_csv

student_data.to_csv('student_data.csv')