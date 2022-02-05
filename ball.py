from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_incr = random.choice([-10, 10])
        self.y_incr = random.randint(-7, 7)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_incr
        new_y = self.ycor() + self.y_incr
        self.setposition(new_x, new_y)

    def wall_bounce(self):
        self.y_incr = self.y_incr * -1

    def paddle_bounce(self):
        self.x_incr = self.x_incr * -1

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_incr = self.x_incr * -1

    def increase_speed(self):
        self.move_speed *= 0.9


