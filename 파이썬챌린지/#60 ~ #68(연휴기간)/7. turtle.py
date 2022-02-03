import turtle

turtle.shape('turtle')

for i in range(0, 5):
    turtle.forward(100)
    # 선을 그리고 나서 향하는 방향
    turtle.right(72)

turtle.exitonclick()


# 60
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

# 사용자가 터틀윈도우를 클릭하면 윈도우가 자동으로 닫힌다
#turtle.exitonclick()

# 61 삼각형
for i in range(0, 3):
    turtle.forward(100)
    turtle.right(120)

turtle.exitonclick()

# 62 원
for i in range(0, 360):
    turtle.forward(1)
    turtle.right(1)


#63 정사각형 3개
#도형의 외곽선, 채우기
turtle.color("black","red")
# 도형 코드 앞에, 그리는 모양 안을 채우기 시작
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
# 선 안그리기
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()

turtle.color("black",'yellow')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()

turtle.color("black",'green')
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
# 없으면 색깔안채워짐
turtle.end_fill()
turtle.forward(100)
turtle.pendown()


#64 별
for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)




#65 숫자 123, 나

turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.backward(100)
turtle.right(270)
turtle.forward(50)
turtle.pendown()

#2
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
turtle.right(270)
turtle.forward(100)
turtle.pendown()

turtle.right(90)
turtle.forward(100)
turtle.right(90)

turtle.forward(50)
turtle.right(90)

turtle.forward(70)
turtle.backward(70)
turtle.left(90)

turtle.forward(50)
turtle.right(90)

turtle.forward(100)

turtle.exitonclick()


#66 각 선 색상을 다르게 하여(무작위 선택) 팔각형
import random

turtle.pensize(3)
for i in range(0, 8):
    turtle.color(random.choice(['red','blue','yellow','pink','blue','orange']))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()


#67 패턴

for x in range(0, 10):
    for i in range(0, 8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

# 다 그리고 거북이 사라짐
turtle.hideturtle()
turtle.exitonclick()


#68 프로그램 시작할때마다 변경되는 패턴, random 함수를 사용하여 선의 개수, 길이, 회전 각도 선택
#멀쩡한 도형일 필요는 없음, 그냥 움직이기만 하면 됨

lines = random.randint(5, 20)
for x in range(0, lines):
    length = random.randint(25, 100)
    rotate = random.randint(1, 365)
    turtle.forward(length)
    turtle.right(rotate)
turtle.exitonclick()
