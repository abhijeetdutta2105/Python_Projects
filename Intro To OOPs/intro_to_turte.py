# turtle is a graphics module
from turtle import Turtle, Screen

# lets grab the Turtle class inside turtle module
timmy = Turtle()

# You can change the shape of the turtle to arrow, circle, turtle and some other shapes provided
timmy.shape("turtle")
# Screen is actually for the window where turtle is going to show up

my_screen = Screen()

print(f"Height: {my_screen.canvheight}")
print(f"Width: {my_screen.canvwidth}")

# By default, the screen just pops up and exits but doing exitonclick() it will only exit if we click on the screen
timmy.forward(100)
timmy.circle(10)

# you can change the color of the brush too
timmy.color("blue")
timmy.back(100)
my_screen.exitonclick()



