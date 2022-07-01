from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

x = 0.1
game_on = True
while game_on:
    ball.move_ball()
    time.sleep(x)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        x *= 0.9

    if ball.xcor() > 380:
        score.score_l()
        score.score_update()
        time.sleep(0.5)
        ball.new_life()
        x = 0.1
    elif ball.xcor() < -380:
        score.score_r()
        score.score_update()
        time.sleep(0.5)
        ball.new_life()
        x = 0.1





screen.exitonclick()