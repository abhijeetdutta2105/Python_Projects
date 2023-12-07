# TODO 1 : Create a Snake Body and import it from snake.py

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("My Snake Game")
# tracer() turns the animation on/off. For off put 0
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# TODO 3: Control the snake with Up, Down, Left and Right Keys

screen.listen()
# controlling by Up, Down, Left and Right keys
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

# TODO 2: Move the snake
is_game_on = True

# update() performs the turtle screen update. Used when tracer is turned off
while is_game_on:
    screen.update()
    time.sleep(0.1)  # introduce a delay
    snake.move()

    # TODO 4: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # TODO 5: Create a scoreboard
        snake.increase_length()
        scoreboard.increase_score()

    # TODO 6: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        is_game_on = False

    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False

# TODO 7: Detect collision with tail
    for segment in snake.segments[1:]:
        # we don't start from first segment because itself is a head, hence we performed slicing
        if snake.head.distance(segment) < 10:
            is_game_on = False

    if not is_game_on:
        scoreboard.game_over()

screen.exitonclick()
