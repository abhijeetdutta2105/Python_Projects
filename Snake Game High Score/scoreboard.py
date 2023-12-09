from turtle import Turtle
SCORE_POSITION = 'center'
SCORE_FONT = ('Courier', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color('white')
        self.penup()
        self.goto(x=0, y = 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score : {self.score} High Score : {self.high_score}', align=SCORE_POSITION, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    def get_high_score(self):
        with open('high_score.txt') as file:
            contents = file.read()
            return int(contents)
    def reset(self):
        self.high_score = max(self.score, self.high_score)
        with open(file='high_score.txt',mode='w') as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg='GAME OVER!', align=SCORE_POSITION, font=SCORE_FONT)
