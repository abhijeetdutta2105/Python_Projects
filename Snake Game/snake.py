from turtle import Turtle

STARTING_X_POS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment(STARTING_X_POS[i])

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.setposition(position, 0)
        self.segments.append(new_segment)

    def increase_length(self):
        self.add_segment(self.segments[-1].position()[0])

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    # you only need to move the first segment and the rest follows it
    def up(self):
        # we did these checks to preserve the original snake game flavor
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)