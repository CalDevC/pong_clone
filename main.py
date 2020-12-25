from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import random

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Objects
r_paddle = Paddle()
r_paddle.goto(370, 0)

l_paddle = Paddle()
l_paddle.goto(-370, 0)

ball = Ball()

score_board = Score()

# Event listening
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect if ball contacted top or bottom
    if ball.ycor() >= 300:
        ball.goto(ball.xcor(), 300)
        ball.setheading(ball.heading() + random.randrange(100, 180))

    if ball.ycor() <= -300:
        ball.goto(ball.xcor(), -300)
        ball.setheading(ball.heading() + random.randrange(100, 180))

    # Detect if point was scored, increment score, and reset ball
    if ball.xcor() >= 390:
        score_board.add_l_point()
        ball.reset()
    elif ball.xcor() <= -390:
        score_board.add_r_point()
        ball.reset()

    # Detect if paddle contacted ball
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 360:
        ball.goto(360, ball.ycor())
        ball.setheading(ball.heading() + random.randrange(100, 180))

    if ball.distance(l_paddle) < 50 and ball.xcor() <= -360:
        ball.goto(-360, ball.ycor())
        ball.setheading(ball.heading() + random.randrange(100, 180))

screen.exitonclick()
