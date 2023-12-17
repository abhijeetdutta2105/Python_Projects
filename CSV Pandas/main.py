import turtle
from turtle import Turtle, Screen

import pandas

screen = Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# this was the way to get the coordinates of the states
# def get_mouse_click_coord(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coord)
#
# turtle.mainloop()

# but lucky for us, we already have it in 50_states.csv

is_game_on = True
score = 0
correct_guess = []
states_data = pandas.read_csv('50_states.csv')
states = states_data['state'].to_list()

while is_game_on:
    answer_state = screen.textinput(title='Guess the State', prompt='What is the another state?').title()
    if answer_state in states:
        score += 1
        correct_guess.append(answer_state)
        screen.title(f'Score : {score}/50')

        # now we need to write up the text
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = states_data[states_data.state == answer_state]
        x = states_data[states_data.state == answer_state]['x'].to_list()[0]
        # y = states_data[states_data.state == answer_state]['y'].to_list()[0]
        y = state_data.y.item()
        # the below calling to single element Series is deprecated and will cause future error hence only use the above
        # x = int(state_data.x)
        # y = int(state_data.y)
        # or you can do state_data.x.item()
        tim.goto(x,y)
        tim.write(answer_state)

    if score == 50 or answer_state == 'Exit':
        is_game_on = False
    else:
        screen.title(f'Score : {score}/50')
        continue

# generate a state_to_learn.csv for missed states
states = list(set(states).difference(set(correct_guess)))

missed_states = pandas.DataFrame(states)
missed_states.to_csv('state_to_learn.csv')
turtle.exitonclick()
