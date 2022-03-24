from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(6, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.sety(self.ycor() + 30)

    def go_down(self):
        self.sety(self.ycor() - 30)
