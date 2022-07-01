from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.movx = 10
        self.movy = 10

    def move_ball(self):
        new_x = self.xcor() + self.movx
        new_y = self.ycor() + self.movy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.movy *= -1

    def bounce_x(self):
        self.movx *= -1

    def new_life(self):
        self.goto(0, 0)
        self.bounce_x()
