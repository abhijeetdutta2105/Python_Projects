# Sketch App
# TODO: W : Forward, S : Backward, A : Left, D : Right, C : clear and go to home
from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.forward(50)


def move_backward():
    timmy.back(50)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def do_reset():
    timmy.home()
    timmy.clear()


my_screen = Screen()
my_screen.listen()
my_screen.onkey(key='w', fun=move_forward)
my_screen.onkey(key='s', fun=move_backward)
my_screen.onkey(key='a', fun=turn_left)
my_screen.onkey(key='d', fun=turn_right)
my_screen.onkey(key='c', fun=do_reset)
my_screen.exitonclick()
