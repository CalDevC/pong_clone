from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.write(f"{self.l_score}     {self.r_score}", align=ALIGNMENT, font=FONT)


    def add_l_point(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", align=ALIGNMENT, font=FONT)

    def add_r_point(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", align=ALIGNMENT, font=FONT)