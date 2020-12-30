from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -290)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -290)
