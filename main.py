from turtle import Screen
from paddle import Paddle

STARTING_X1 = -350
STARTING_Y = 0
STARTING_X2 = 350

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()


paddle_l = Paddle((STARTING_X1, STARTING_Y))
paddle_r = Paddle((STARTING_X2, STARTING_Y))

game_is_on = True
while game_is_on:

    screen.onkeypress(paddle_l.go_up, "w")
    screen.onkeypress(paddle_r.go_up, "Up")

    screen.onkeypress(paddle_l.go_down, "s")
    screen.onkeypress(paddle_r.go_down, "Down")

    screen.update()

screen.exitonclick()
