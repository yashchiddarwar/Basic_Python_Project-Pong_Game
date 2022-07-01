from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(100, 230)
        self.write(f"{self.l_score}", False, "center", ('Arial', 40, 'normal'))
        self.goto(-100, 230)
        self.write(f"{self.r_score}", False, "center", ('Arial', 40, 'normal'))
    # def gameover(self):
    #     self.color("white")
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", False, "center", ('Arial', 25, 'normal'))

    def score_l(self):
        self.l_score += 1
        self.score_update()

    def score_r(self):
        self.r_score += 1
        self.score_update()



    # def score_update(self, r_l):
    #     self.clear()
    #     self.color("white")
    #     self.score = self.score + 1
    #     if r_l == "r":
    #         self.hideturtle()
    #         self.goto(100, 250)
    #         self.write(f"{self.score}", False, "center", ('Arial', 25, 'normal'))
    #     else:
    #         self.hideturtle()
    #         self.goto(-100, 250)
    #         self.write(f"{self.score}", False, "center", ('Arial', 25, 'normal'))

