# if you don't use mode = 'a' then it would overwrite on the file
# using 'a' means appending what you write
# also by default mode = 'r' so you need to use 'w' or 'a' for writing to the file

# also if you try to open a file which does not exist in write mode then that file would be created for you

with open('my_file.txt','a') as file:
    file.write('\nI want to improve the snake game via saving high score in files')
