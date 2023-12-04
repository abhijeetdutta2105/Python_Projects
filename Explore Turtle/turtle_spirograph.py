import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
my_screen = Screen()
turtle.colormode(255)


def random_color():
    """This will return a random tuple of red, blue and green for the color"""
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)

    return (red, blue, green)


# we can draw a spirograph
def draw_spirograph(gap):
    tom.speed('fastest')
    for step in range(360 // gap):
        tom.color(random_color())
        tom.circle(100)
        tom.left(gap)


# draw_spirograph(5)

my_screen.exitonclick()
