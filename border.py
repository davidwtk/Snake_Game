# This module makes the walls of the game.
from turtle import Turtle
SPEED = 0
BORDER_COORDS = [(-280, -280), (280, -280), (280, 280), (-280, 280)]
BORDER_COLOUR = "White"


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(BORDER_COLOUR)
        self.penup()
        self.speed(SPEED)

    def draw_border(self):
        BORDER_COORDS.append(BORDER_COORDS[0])
        for coords in BORDER_COORDS:
            self.setpos(coords)
            self.pendown()

