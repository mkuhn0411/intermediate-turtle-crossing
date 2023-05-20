from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()

    def turtle_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)

    def successful_cross(self):
        return self.ycor() > FINISH_LINE_Y

    def setup(self):
        self.up()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.go_to_starting_position()