from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard
from border import Border

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)

b1 = Border()
b1.draw_border()

s1 = Snake()
f1 = Food()
c1 = ScoreBoard()

s.listen()
s.onkey(fun=s1.go_up, key="Up")
s.onkey(fun=s1.go_down, key="Down")
s.onkey(fun=s1.go_left, key="Left")
s.onkey(fun=s1.go_right, key="Right")

snake_alive = True
while snake_alive:
    s.update()
    time.sleep(0.1)
    s1.move()
    if s1.head.distance(f1) < 15:
        c1.score_update()
        f1.refresh_location()
        s1.extend()
    elif s1.head.xcor() < -280 or s1.head.xcor() > 280 or s1.head.ycor() < -280 or s1.head.ycor() > 280:
        c1.game_over()
        snake_alive = False

    for segments in s1.sp[1:]:
        if s1.head.distance(segments) < 10:
            c1.game_over()
            snake_alive = False

s.exitonclick()
