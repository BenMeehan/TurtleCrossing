from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-350, 280)
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'GAME OVER!',
                   align='center', font=('Arial', 30, 'normal'))

    def update(self):
        self.level += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f'Level : {self.level}',
                   align='left', font=('Arial', 15, 'normal'))
