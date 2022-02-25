from turtle import Screen, Turtle
from paddle import  Paddles
from ball import Balls
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
screen.tracer(0)

screen.listen()

r_paddle = Paddles((-350, 0))
l_paddle = Paddles((350, 0))
ball = Balls()

screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()