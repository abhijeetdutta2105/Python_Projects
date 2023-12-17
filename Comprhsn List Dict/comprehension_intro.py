# comprehension of list and dictionary is very unique to python.
# It is used to make the code a lot shorter and sometimes readable

# so to create a list from an existing collection or list using minimal line of code is list comprehension
"""
Syntax:
list = [some existing collection]
new_list = [new_item for item in list if condition]
"""
# Dictionary Comprehension
"""
Syntax:
iterable_seq = []
new_dict = {key : value for item in iterable_seq if condition}
"""
# But not always are the comprehensions easy to read. So, only if you are sure you could use it.

# There is method called zip(list1, list2) which takes two lists and forms a zip object out of it
student_name = ['Aman','Ram','Akshat','Varun']
student_marks = [50,60,70,80]
student_info = {name : marks for (name,marks) in zip(student_name,student_marks)}
print(f'The student information is {student_info}')

# for iterating through pandas dataframe you can use .iterrows() to iterate through row of the dataframe
# means accessing the (index,series) as a tuple
# for more info check the NATO_alphabet.py