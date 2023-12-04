import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()
my_screen = Screen()

turtle_colors = ['blue','brown', 'green', 'orange', 'pink', 'gold', 'purple']
def draw_shape(sides, angle):
    for step in range(sides):
        timmy.forward(100)
        timmy.right(angle)

def draw_shape_another(sides, angle):
    for step in range(sides):
        timmy.forward(100)
        timmy.left(angle)

# you can draw different shapes based on different angles and sides

# triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# instead of manually calculating the angle using formula you can do it pretty quickly
# internal_angle = 360 / sides
draw_shape(3, 120)
draw_shape(4, 90)
draw_shape(5, 72)
draw_shape(6, 60)
draw_shape(7, 51.43)
draw_shape(8, 45)
draw_shape(9, 40)
draw_shape(10, 36)

# this is the smart code which you should employ
# you have even changed the color after every shape
for side in range(3, 11):
    angle = 360 / side
    draw_shape_another(side, angle)
    timmy.color(random.choice(turtle_colors))

my_screen.exitonclick()
