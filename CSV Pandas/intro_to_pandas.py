# Pandas is a popular python library that is used of analysis of data
# CSV stands for comma separated values. They are pretty helpful in representing tabular data.

# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# but the above is still pretty difficult to work with. We have an inbuilt library csv for our ease

# import csv
#
# with open('weather_data.csv') as data_file:
#     temperatures = []
#     data = csv.reader(data_file)
#     for row in data:
#         if 'temp' in row:
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

# above is still pretty neat but still a lot of processing of even a single row of data
# now let's finally use the package we were waiting for
import pandas

data = pandas.read_csv('weather_data.csv')
print(data['day'])
print(data)