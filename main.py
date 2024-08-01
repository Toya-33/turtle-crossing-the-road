import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=player.move)
game_is_on = True
while game_is_on:
    time.sleep(car_manager.speed)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect finished line
    if player.finished():
        scoreboard.level_up()
        car_manager.increase_speed()
        player.refresh()


screen.exitonclick()

