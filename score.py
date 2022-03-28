# This module makes a scoreboard to track the current score.
from turtle import Turtle
FONT_TYPE = ("Algerian", 14, "bold")
ALIGNMENT = "center"
SCORE_COLOUR = "Green"
SCORE_POSITION = 0, 280


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor(SCORE_COLOUR)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(SCORE_POSITION)
        self.pendown()
        self.write(arg=f"Score: 0", align=ALIGNMENT, font=FONT_TYPE)

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT_TYPE)

    def game_over(self):
        self.penup()
        self.home()
        self.pendown()
        self.pencolor("Maroon")
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT_TYPE)
