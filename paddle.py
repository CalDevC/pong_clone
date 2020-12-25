from turtle import Turtle

SPEED = 50

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + SPEED)

    def down(self):
        self.goto(self.xcor(), self.ycor() - SPEED)
