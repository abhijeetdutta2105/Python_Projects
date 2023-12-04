from turtle import Turtle, Screen

# sometimes if the package or class name gets long you can work with alias too (using the 'as' keyword)
# from package_name import class_name as cls
# in good python code you should not use from package_name import *
# the above creates confusion along the way

# turtle module relies on tkinter to create the graphics

timmy = Turtle()
my_screen = Screen()


# Let's draw a triangle
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)

# changing color of the object
timmy.color('red')

# drawing circle of the radius
timmy.circle(20)

timmy.shape('circle')
timmy.backward(100)

# changing back the shape and creating a square
timmy.shape('turtle')
for step in range(4):
    timmy.forward(100)
    timmy.left(90)

# clearscreen() clears everything, clear() also does the same
# reset() is used to reset everything back to default
# my_screen.clearscreen()
my_screen.reset()

# drawing a dashed line
# 1st way using colors black and white
for step in range(10):
    timmy.forward(10)
    timmy.color('white')
    timmy.forward(10)
    timmy.color('black')

my_screen.reset()
# 2nd way using up() method of turtle
# which means there would be no drawing when moving and down() when you want to draw again
for step in range(10):
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)
    timmy.down()

my_screen.exitonclick()