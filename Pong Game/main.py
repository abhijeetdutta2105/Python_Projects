# pong is classic game where paddle hits the ball and misses are counted as score
# TODO 1: Create the screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# TODO 2: Create and move a paddle
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball(0,0)
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')

# TODO 3: Create another paddle
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()

    # TODO 4: Create the ball and make it move
    ball.move()
    # TODO 5: Detect collision with wall and bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 6: Detect collision with paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 7: Detect when paddle misses
    # TODO 8: Keep Score
    elif ball.xcor() > 380: # right paddle misses
        ball.restart()
        scoreboard.l_point()

    elif ball.xcor() < -380: # left paddle misses
        ball.restart()
        scoreboard.r_point()


screen.exitonclick()