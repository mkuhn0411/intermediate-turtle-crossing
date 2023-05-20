import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)


def screen_listener(player, car_manager):
    screen.listen()
    screen.onkey(player.turtle_up, "Up")


def turtle_hit(player, cars):
    for car in cars:
        if car.distance(player) < 20:
            return True

    return False


def cars_past_edge(cars):
    all_past_edge = True

    for car in cars:
        if car.xcor() > -300:
            all_past_edge = False

    return all_past_edge


def run():
    game_is_on = True
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    screen_listener(player, car_manager)

    while game_is_on:
        time.sleep(0.1)
        screen.update()

        # detect if turtle is hit
        if turtle_hit(player, car_manager.cars):
            scoreboard.write_score(True)
            game_is_on = False
        # detects a successful crossing
        elif player.successful_cross():
            scoreboard.add_to_score()
            car_manager.increase_car_speed()
            player.go_to_starting_position()
        else:
            random_chance = random.randint(1, 6)
            random_chance == 1 and car_manager.create_car()
            car_manager.move_cars()


run()

screen.exitonclick()
