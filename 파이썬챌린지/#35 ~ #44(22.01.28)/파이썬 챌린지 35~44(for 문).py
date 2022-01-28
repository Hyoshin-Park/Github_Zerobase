#35

name = input("Enter your name: ")

for i in range(1, 4):
    print(f"Your name is {name}")

#36

name = input("Enter your name: ")
numberOfTime = int(input("Enter how many times: "))

for i in range(1, numberOfTime + 1):
    print(f"Your name is {name}")

#37

name = input("Enter your name: ")

for i in name:
    print(i)

#38

name = input("Enter your name: ")
numberOfTime = int(input("Enter how many times: "))
for x in range(1, numberOfTime + 1):
    for i in name:
        print(i)

# 39

number = int(input("Enter number between 1 and 12: "))
for i in range(number, 13):
    i *= 12
    print(i)

#40

number = int(input("Enter number under 50: "))

for i in range(50, number - 1, -1):
    print(i)

#41

name = input("Enter your name: ")
number = int(input("Enter a number: "))

if number < 10:
    for num in range(1, number + 1):
        print(name)
if number >= 10:
    for i in range(1, 4):
        print("Too high")

#42

total = 0

for i in range(0, 5):
    num = int(input("Enter a number: "))
    print("1) Plus or \n2) Don`t plus ")
    num1 = int(input("Enter a number: "))
    if num1 == 1:
        total += num
    if num1 == 2:
        continue

print(total)

#43

print("1) Count up or \n2) Count down ")
num1 = int(input("Enter a number: "))

if num1 == 1:
    num2 = int(input("Enter a large number: "))
    for i in range(1, num2 +1):
        print(i)
elif num1 == 2:
    num3 = int(input("Enter a number under 20: "))
    for i1 in range(20, num3 - 1, -1):
        print(i1)
else:
    print("I don`t understand")

#44

print("How many people do you want to invite?")
num1 = int(input("Enter how many: "))
if num1 < 10:
    for i in range(0, num1):
        name = input("Enter how name: ")
        print(f"{name} has been invited")
elif num1 > 10:
    print("Too many people")
