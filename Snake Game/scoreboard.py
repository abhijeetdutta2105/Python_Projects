from turtle import Turtle
SCORE_POSITION = 'center'
SCORE_FONT = ('Courier', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y = 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f'Score : {self.score}', align=SCORE_POSITION, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER!', align=SCORE_POSITION, font=SCORE_FONT)
