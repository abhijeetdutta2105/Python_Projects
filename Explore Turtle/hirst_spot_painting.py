# we will install and use colorgram module to extract colors from an image
import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
# #colorgram.extract() takes 2 arguments: file name and number of colors to extract
# colors = colorgram.extract('hirst_painting\spot_painting.jpeg', 30)
# extracted_colors = []
# # print(colors[0].rgb) , the .rgb extracts the red, green, blue component
#
# for color in colors:
#     required_color = (color.rgb[0], color.rgb[1], color.rgb[2])
#     extracted_colors.append(required_color)
#
# print(extracted_colors)
turtle.colormode(255)  # this is must to set the colormode or we will get error
color_list = [(134, 78, 67), (71, 98, 114), (214, 145, 93), (215, 63, 125), (26, 61, 55), (103, 164, 174), (56, 88, 74),
              (178, 55, 75), (245, 204, 61), (100, 101, 169), (39, 76, 67), (240, 172, 181), (42, 55, 60),
              (196, 130, 162), (137, 168, 164), (86, 155, 161), (178, 89, 83), (70, 42, 34), (36, 74, 78), (95, 51, 43),
              (92, 153, 150), (132, 37, 48), (217, 179, 175), (174, 201, 197), (166, 203, 208), (182, 184, 209)]

timmy = Turtle()
my_screen = Screen()
# setheading(0) means go to east direction

def draw_left(column):
    timmy.setheading(0)

    for step in range(column):
        timmy.pencolor(random.choice(color_list))
        timmy.dot(20)
        timmy.forward(50)
    timmy.backward(50)
    timmy.left(90)
    timmy.forward(50)


def draw_right(column):
    timmy.setheading(0)
    for step in range(column):
        timmy.pencolor(random.choice(color_list))
        timmy.dot(20)
        timmy.backward(50)
    timmy.forward(50)
    timmy.right(90)
    timmy.backward(50)


timmy.up()
timmy.speed('fastest')
# let's hide our turtle too
timmy.hideturtle()
row, col = 7, 5

counter = 0
while counter < row:
    draw_left(col)
    counter += 1
    if counter == row:
        break
    draw_right(col)
    counter += 1

my_screen.exitonclick()
