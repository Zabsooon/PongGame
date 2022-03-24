from turtle import Screen
from paddle import Paddle
from ball import Ball

STARTING_X1 = -350
STARTING_Y = 0
STARTING_X2 = 350


def reset_positions():
    paddle_l.goto(STARTING_X1, STARTING_Y)
    paddle_r.goto(STARTING_X2, STARTING_Y)
    ball.reset_position()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()


paddle_l = Paddle((STARTING_X1, STARTING_Y))
paddle_r = Paddle((STARTING_X2, STARTING_Y))

ball = Ball()

game_is_on = True
while game_is_on:

    # Paddles movement events:
    screen.onkey(paddle_l.go_up, "w")
    screen.onkey(paddle_r.go_up, "Up")

    screen.onkey(paddle_l.go_down, "s")
    screen.onkey(paddle_r.go_down, "Down")

    # Ball movement events:
    ball.change_position()

    # Ball wall bouncing:
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    elif ball.xcor() > 380:   # score!
        reset_positions()
    elif ball.xcor() < -380:  # score!
        reset_positions()
    elif ball.distance(paddle_l) < 50 and ball.xcor() < -340 or ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    screen.update()


screen.exitonclick()
