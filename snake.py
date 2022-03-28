# This module generates the snake object and adds segments when eating food.
from turtle import Turtle
XCOORD = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.sp = []
        self.create_snake()
        self.head = self.sp[0]

    def create_snake(self):
        for position in XCOORD:
            self.add_segment(position)

    def move(self):
        for segment in range(len(self.sp) - 1, 0, -1):
            new_x = self.sp[segment - 1].xcor()
            new_y = self.sp[segment - 1].ycor()
            self.sp[segment].setpos(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        t = Turtle("square")
        t.color("green")
        t.penup()
        t.speed(0)
        t.setpos(position)
        self.sp.append(t)

    def extend(self):
        self.add_segment(self.sp[-1].pos())

