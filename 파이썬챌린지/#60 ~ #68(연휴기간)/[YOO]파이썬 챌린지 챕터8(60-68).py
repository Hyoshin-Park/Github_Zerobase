#60
import turtle

for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()


#61
import turtle

for i in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.exitonclick()


#62번
import turtle

for i in range(360):
    turtle.forward(1)
    turtle.right(1)

turtle.exetonclick()


#63번
import turtle
turtle.color("black", "red")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()

turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()

turtle.color("black", "blue")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)

turtle.end_fill()



#64번
import turtle

for i in range(5):
    turtle.forward(100)
    turtle.right(144)



#65번
import turtle

turtle.left(90)
turtle.forward(100)
turtle.right(90)

turtle.penup()
turtle.forward(50)

turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.forward(50)

turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.right(180)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)

turtle.exitonclick()



#66번
import random
import turtle

color = random.choice(['red','yellow','blue','black','green','purple'])

for i in range(8):
    color = random.choice(['red','yellow','blue','black','green','purple'])
    turtle.color(f"{color}")
    turtle.forward(100)
    turtle.right(45)
turtle.exitonclick()


#67번
import turtle
for i in range(12):
    for i in range(8):
        turtle.forward(100)
        turtle.right(45)
    turtle.right(30)
turtle.exitonclick()



#68번
import random
import turtle

a = random.randint(1, 8)


for i in range(a):
    b = random.randrange(10,100,10)
    c = random.randrange(20,360,20)
    turtle.forward(b)
    turtle.right(c)

turtle.exitonclick()