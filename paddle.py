from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.setposition(x_cor, y_cor)

    def move_up(self):
        if 350 > self.ycor():
            new_y = self.ycor() + 20
            self.sety(new_y)

    def move_down(self):
        if -340 < self.ycor():
            new_y = self.ycor() - 20
            self.sety(new_y)
