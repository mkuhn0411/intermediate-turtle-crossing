from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("deep pink")
        self.up()
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()

    def write_score(self, turtle_hit=False):
        if turtle_hit:
            self.goto(0, 0)
            self.write(f"Game over, you hit a turtle!", align=ALIGNMENT, font=FONT)
        else:
            self.clear()
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_to_score(self):
        self.score += 1
        self.write_score()