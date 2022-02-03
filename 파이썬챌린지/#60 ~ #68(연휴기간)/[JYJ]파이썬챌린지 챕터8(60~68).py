# 060

import turtle

for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)

print(turtle.exitonclick())

# 061

import turtle

for i in range(0, 3):
    turtle.forward(50)
    turtle.right(120)

print(turtle.exitonclick())

# 062

import turtle

for i in range(0, 360):
    turtle.forward(1)
    turtle.right(1)

print(turtle.exitonclick())

# 063

import turtle

turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)
    turtle.color('black', 'red')
turtle.penup()
turtle.forward(100)
turtle.end_fill()

turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)
    turtle.color('black', 'blue')
turtle.penup()
turtle.forward(100)
turtle.end_fill()

turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)
    turtle.color('black', 'yellow')
turtle.penup()
turtle.forward(100)
turtle.end_fill()


print(turtle.exitonclick())

# 064

import turtle

for i in range(0, 5):
    turtle.forward(30)
    turtle.right(144)

print(turtle.exitonclick())

# 065

import turtle

turtle.left(90)
turtle.forward(90)
turtle.right(90)

turtle.penup()
turtle.forward(90)

turtle.pendown()
turtle.forward(90)
turtle.right(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(90)

turtle.penup()
turtle.forward(90)

turtle.pendown()
turtle.forward(90)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(60)
turtle.left(180)
turtle.forward(60)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(90)

print(turtle.exitonclick())

# 066

import turtle
import random

for i in range(0, 8):
    turtle.color(random.choice(['Yellow', 'red', 'blue', 'green', 'navy', 'black', 'pink', 'purple']))
    turtle.forward(50)
    turtle.right(360 / 8)

print(turtle.exitonclick())

# 067

import turtle

for i in range(0, 10):
    for j in range(0, 8):
        turtle.forward(50)
        turtle.right(360 / 8)
    turtle.right(360 / 10)

print(turtle.exitonclick())

# 068
import turtle
import random

line = random.randint(10, 20)

for i in range(line):
    length = random.randint(20, 100)
    angle = random.randint(1, 365)
    turtle.forward(length)
    turtle.right(angle)

print(turtle.exitonclick())