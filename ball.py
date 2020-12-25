from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.last_set_heading = 45

    def move(self):
        self.forward(5)

    def reset(self):
        if self.last_set_heading == 45:
            self.goto(0, 0)
            self.last_set_heading = 225
            self.setheading(self.last_set_heading)
        else:
            self.last_set_heading = 45
            self.setheading(self.last_set_heading)
            self.goto(0, 0)
