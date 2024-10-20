from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()



screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.x_bounce()

    #Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    #Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()