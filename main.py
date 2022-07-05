# import colorgram
# colors = colorgram.extract('image.jpg', 20)
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)
import turtle
from turtle import Turtle, Screen
import random


color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]

tim = Turtle()
screen = Screen()
tim.speed("fastest")
turtle.colormode(255)
tim.penup()
tim.hideturtle()


for y in range(250, -250, -50):
    for x in range(-250, 250, 50):
        tim.goto(x,y)
        tim.dot(20, random.choice(color_list))

screen.exitonclick()
