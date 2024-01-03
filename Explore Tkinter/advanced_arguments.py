# sometimes it is necessary to have default value for arguments

# so if needed you can only modify the required ones

# let's have functions that can have any number of arguments
# *args says that the arguments can accept multiple inputs in form of a tuptle

# so in this way you can have unlimited positional arguments
def add_nums(*args):
    return sum(args)

print(add_nums(1,2,3,4,5))

# now let's create unlimited keyword arguments
# in the hood it will have a dictionary where you can have keywords as keys the input values as its values

def fill_details(**kwargs):
    print(kwargs)

fill_details(name='Abhijeet',age=22, langauge='Java')

# in dict there is a tip you can follow try to use dict_name.get(key_name) in place of dict[key_name]
# because the latter gives an error while the former gives None if the key does not exist

class Car:
    def __init__(self,**kwargs):
        self.model = kwargs.get('model')
        self.make = kwargs.get('make')

my_car = Car(model='latest',make='Nissan')


# now kwargs are the reason why you won't see any quick support documentation for tkinter functions
# tkinter was derived from Tk whose syntax is completely different
# so keyword arguments were used to set the properties
