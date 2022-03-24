from turtle import Turtle

ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=("courier", 75, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=("courier", 75, "normal"))

    def add_point_l(self):
        self.l_score += 1
        self.refresh()

    def add_point_r(self):
        self.r_score += 1
        self.refresh()