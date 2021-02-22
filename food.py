from turtle import Turtle
from random import randint

FOOD_COLOR = "red"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(FOOD_COLOR)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 265)
        self.goto(rand_x, rand_y)
