import turtle
from turtle import Turtle, Screen
import random

turtle_colors = ['blue', 'brown', 'green', 'orange', 'pink', 'gold', 'purple']
directions = [0, 90, 180, 270]
timmy = Turtle()
my_screen = Screen()
turtle.colormode(255)


def random_color():
    """This will return a random tuple of red, blue and green for the color"""
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)

    return red, blue, green


# to alter the width and speed of turtle, speed ranges are limited 0 - 10
# setheading() gives random direction to the turtle

def random_walk():
    timmy.width(3)
    timmy.speed(10)
    for step in range(100):
        angle = random.choice(directions)
        timmy.color(random.choice(turtle_colors))
        timmy.setheading(angle)
        timmy.forward(30)

    my_screen.reset()


# random_walk()

# let's pick some random colors not just restricted to a list we choose
def test_func():
    turtle.speed('slow')
    turtle.forward(100)
    turtle.color(random_color())
    turtle.back(100)
my_screen.exitonclick()
