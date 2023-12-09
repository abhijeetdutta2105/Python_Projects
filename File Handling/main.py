'''Mail Merge Challenge'''

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt, replace the placeholder
# create the letter and save it to ReadyToSend directory


# let us work on each name of the invited_names.txt file
with open(file='invited_names.txt') as name_file:
    for name in name_file:
        # this will store line by line content of the starting_letter.txt
        name = name.strip()
        contents = []
        with open(file='starting_letter.txt') as file:
            # alternatively you can directly use readlines() function to do the same
            # for line in file:
            #     contents.append(line)
            contents = file.readlines()

        req_line = ''
        index = 0
        for line in contents:
            if '[name]' in line:
                req_line = line
                break
            index += 1

        req_line = req_line.replace('[name]',name)

        contents[index] = req_line

        f = open(f'ReadyToSend/letter_for_{name}.txt','a')
        for line in contents:
            f.write(line)

        f.close()



