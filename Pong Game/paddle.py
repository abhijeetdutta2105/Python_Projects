from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape('square')
        self.color('white')
        self.goto(x=x_pos, y=y_pos)

    def up(self):
        prev_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(prev_x, new_y)

    def down(self):
        prev_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(prev_x, new_y)
