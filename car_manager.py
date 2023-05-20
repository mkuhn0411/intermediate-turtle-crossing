from turtle import Turtle
import random

COLORS = ["red", "crimson", "orange", "dark orange", "orange red", "yellow", "green", "lawn green", "sea green", "medium spring green", "blue", "royal blue", "medium blue", "dodger blue", "purple", "blue violet", "medium slate blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX = 280


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        car = Turtle("square")
        car.up()
        car.shapesize(1, 2)
        car.setheading(180)
        car.color(random.choice(COLORS))
        y_index = random.randint(-250, 250)
        car.goto(300, y_index)
        self.cars.append(car)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

