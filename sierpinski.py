from turtle import Turtle, Screen
import constants as const
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title('SIERPINSKI TRIANGLE')

outer = const.OUTER_POINTS

levi = Turtle()

def draw_outer():
    levi.penup()
    levi.goto(const.STARTING_POINT)
    levi.pendown()
    for pts in outer:
        levi.goto(pts)
        levi.dot(size = const.DOT_SIZE)
    levi.goto(const.STARTING_POINT)
    levi.dot(size = const.DOT_SIZE)

def start_sierpinksi():
    levi.penup()
    levi.speed(speed=0)
    chosen = const.STARTING_POINT
    for i in range(const.NUMBER):
        outer_tuple = random.choice(outer)
        midpoint = ((outer_tuple[0]+chosen[0])/2, (outer_tuple[1]+chosen[1])/2)
        levi.goto(midpoint)
        levi.dot(size = const.DOT_SIZE)
        chosen = midpoint

#starting the drawing
draw_outer()
start_sierpinksi()

screen.exitonclick()

