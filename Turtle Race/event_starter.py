# event listeners: code that allows us to listen to events

# in turtle, we have screen events functions to help us do it

from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()


def move_forward():
    timmy.forward(100)
    timmy.back(100)


# this will allow to listen for events
my_screen.listen()

# onkey(key,fun) will accept these 2 params and do fun when key will be pressed
# when passing another function as argument to a function we don't use parenthesis for the argument
my_screen.onkey(key='q', fun=move_forward)

# functions which take inputs as another function are called higher-order function
# onkey() is a higher order function
my_screen.exitonclick()
