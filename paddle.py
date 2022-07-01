from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(x, y)

    def up(self):
        posx = self.xcor()
        posy = self.ycor() + 20
        # if 250 > self.ycor() > -250:
        self.goto(posx, posy)

    def down(self):
        posx = self.xcor()
        posy = self.ycor() - 20
        # if 250 > self.ycor() > -250:
        self.goto(posx, posy)
        # else:
        #     posy = self.ycor() + 20

