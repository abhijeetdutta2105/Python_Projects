# Files are important to save data for a long time use
# You should know how to open, read, write and close files

# open(file, mode, encoding) returns a file object
file = open(file='my_file.txt')

contents = file.read() # this returns the content of file as string
print(contents)

# closing the file is important after our work to save resources
file.close()

# you can use file.closed to check if file is open or closed
print(f'Is the file close now: {file.closed}')

print('*'*10)
# another way of opening a file, but you now don't have to close it
with open('my_file.txt') as my_file:
    contents = my_file.read()
    print(contents)

print(f'Is our my_file closed: {my_file.closed}')

