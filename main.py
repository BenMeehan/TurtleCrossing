from turtle import Screen
from car import Car
from player import Player
from score import Score
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('white')
screen.tracer(0)

SPEED = 5

cars = []
game_not_over = True

for i in range(30):
    cars.append(Car())

player = Player()
score = Score()

screen.listen()

screen.onkeypress(player.move, 'Up')


while game_not_over:
    screen.update()
    time.sleep(0.1)

    for i in cars:
        if(i.xcor() < -350):
            i.reset()
        if(player.distance(i) < 30):
            score.game_over()
            game_not_over = False

        i.backward(SPEED*score.level)

    if(player.ycor() > 270):
        score.update()
        player.reset()

screen.exitonclick()
