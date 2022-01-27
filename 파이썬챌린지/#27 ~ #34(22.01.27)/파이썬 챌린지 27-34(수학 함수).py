import math

#27

dight = float(input("Enter a long decimal point: "))

print(f"multply by 2: {dight * 2}")

#28

dight = float(input("Enter a long decimal point: "))

print(f"multply by 2 and round : {round(dight * 2,2)}")

#29

num1 = int(input("Enter number over 500: "))

num1 = math.sqrt(num1)

print(f"square root of num1: {round(num1, 2)}")

#30

pie = float(math.pi)

print(f" pi  equals: {round(pie, 5)}")

#31

radius = int(input("Enter the radius of the circle: "))

pie = math.pi

print(f" area of the circle is: {round((radius ** 2) * pi, 2)}")


#32
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))

pie = math.pi

cylinder = radius * height * pie

print(f"area of the cylinder is {round(cylinder, 3)}")

#33

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number1: "))

quot = num1 // num2

rest = num1 % num2

print(f"{num1} divided by {num2} is {quot} with {rest} remaining")

#34

print("1) Square \n2) Triangle \n")

num1 = int(input("Enter a number: "))

if num1 == 1:
    sHeight = int(input("Enter the length: "))
    print(sHeight ** 2)
elif num1 == 2:
    sHeight = int(input("Enter the length: "))
    sBase = int(input("Enter the base: "))
    print(sHeight * sBase / 2)
else:
    print("enter the correct number.")
