from turtle import Turtle
import random

colors = ['red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'teal', 'brown']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        x = random.randint(350, 1550)
        y = random.randint(-250, 250)
        # self.speed('fastest')
        self.goto(x, y)
        self.color(colors[random.randint(0, len(colors)-1)])

    def reset(self):
        self.setx(random.randint(350, 950))
