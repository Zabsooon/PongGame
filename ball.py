from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.ball_x_direction = 11
        self.ball_y_direction = 11

    def change_position(self):
        self.goto(self.xcor() + self.ball_x_direction, self.ycor() + self.ball_y_direction)
        time.sleep(0.05)

    def bounce_y(self):
        self.ball_y_direction *= -1

    def bounce_x(self):
        self.ball_x_direction *= -1

    def reset_position(self):
        self.bounce_x()  # changes heading of ball at the game start
        self.goto(0, 0)
        time.sleep(0.5)
