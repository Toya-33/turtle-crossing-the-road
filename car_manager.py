from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 0.1

    def create_car(self):
        chance = random.randint(0, 10)
        if chance == 1:
            car = Turtle()
            random_y = random.randint(-250, 250)
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)
            car.goto(300, random_y)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.speed *= 0.5

