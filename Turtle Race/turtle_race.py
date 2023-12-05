# Different objects have different states in terms of their attributes and behaviours
# Let's have a turtle race
from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-100, -60, -20, 20, 60, 100]
my_screen = Screen()

# in this game the dimensions of the screen is crucial. So let's set that up
my_screen.setup(height=400, width=500)
answer = my_screen.textinput(title='Make your bet', prompt='Who will win the race? Enter a color : ')
print(f"You have opted for {answer}")
is_race_on = False
# you can directly put shape here
all_turtles = []
for turtle_object in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_object])
    new_turtle.goto(x=-230, y=y_pos[turtle_object])
    all_turtles.append(new_turtle)

if answer:
    is_race_on = True

while is_race_on:
    distance = random.randint(0,10)
    our_turtle = random.choice(all_turtles)
    our_turtle.forward(distance)
    if our_turtle.pos()[0] >= 230:
        if answer == our_turtle.pencolor():
            print(f"Congrats! Your turtle {answer} won the game")
        else:
            print(f"Sorry! {our_turtle.pencolor()} has won the game")
        is_race_on = False

my_screen.exitonclick()