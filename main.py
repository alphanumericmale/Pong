from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(1200, 800)
s.bgcolor("black")
s.listen()
s.update()
s.title("Pong")
s.tracer(0)

scoreboard = Scoreboard()

paddle_r = Paddle(520, 0)
paddle_l = Paddle(-520, 0)
ball = Ball()

s.onkeypress(paddle_r.move_up, "Up")
s.onkeypress(paddle_r.move_down, "Down")

s.onkeypress(paddle_l.move_up, "w")
s.onkeypress(paddle_l.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if -380 >= ball.ycor():
        ball.wall_bounce()
    if 380 <= ball.ycor():
        ball.wall_bounce()
    if -495 >= ball.xcor() and paddle_l.ycor() - 35 < ball.ycor() < paddle_l.ycor() + 35:
        ball.paddle_bounce()
        ball.increase_speed()
    if 495 <= ball.xcor() and paddle_r.ycor() - 35 < ball.ycor() < paddle_r.ycor() + 35:
        ball.paddle_bounce()
        ball.increase_speed()
    if ball.xcor() < -600:
        scoreboard.l_score += 1
        scoreboard.write_score()
        ball.ball_reset()
    if ball.xcor() > 600:
        scoreboard.r_score += 1
        scoreboard.write_score()
        ball.ball_reset()
    if scoreboard.r_score == 3:
        scoreboard.game_over("RIGHT")
        game_is_on = False
    if scoreboard.l_score == 3:
        scoreboard.game_over("LEFT")
        game_is_on = False



s.exitonclick()

# TODO 5: collision with wall
# TODO 6: collision with paddle
# TODO 7: randomise starting ball motion
# TODO 8: scoreboard
