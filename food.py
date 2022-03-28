# This module generates food particles in random positions.
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh_location()

    def refresh_location(self):
        self.setpos(random.randint(-270, 270), random.randint(-270, 270))
