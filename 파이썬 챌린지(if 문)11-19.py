#12

Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))

if Num1 > Num2:
    print(Num2, Num1)
else:
    print(Num1, Num2)

#12-1

Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))

if Num1 > Num2:
    print(Num2, Num1)
elif Num1 <= Num2:
    print(Num1, Num2)

#13

Num1 = int(input("Enter number lower than 20: "))

    if Num1 >= 20:
        print("Too high")
    else:
        print("Thank you")

#14

Num1 = int(input("Enter number between 10 and 20: "))

if 10 <= Num1 and Num1 <= 20:
    print("Thank you")
else:
    print("Incorrect answer ")

#15

color = input("Enter your favorite color: ")

color = str.lower(color)

if color == "red":
    print("I like red too")
else:
    print("I don`t like the color, I prefer red")

#16

rain = input("Is it raining?: ")

rain = str.lower(rain)

if rain == "yes":
    wind = input("Is it windy? ")
    wind = str.lower(wind)
    if wind == "yes":
        print("It is too windy for an unbrella. ")
    else:
        print("Take an unbrella. ")
else:
    print("Enjoy your day")

#17

age = int(input("How old are you?: "))

if age >= 18:
    print("You can vote.")
elif age == 17:
    print("You can learn to drive.")

elif age == 16:
    print("You can buy a lottery.")
elif age < 16:
    print("You can go Trick or Treating.")

#18

Num1 = int(input("Enter number: "))

if Num1 < 10:
    print("Too low")
elif Num1 >= 10 and Num1 <= 20:
    print("Correct")
else:
    print("Too high")

#18-1 변수 제거

Num1 = input("Enter number: ")

while True:
    try:
        Num1 = int(Num1)
        if Num1 < 10:
            print("Too low")
        elif Num1 >= 10 and Num1 <= 20:
            print("Correct")
        else:
            print("Too high")
        break
    except:
        print("Wrong!, Enter a number")
        break

#19

Num1 = int(input("Enter number: "))

if Num1 == 1:
    print("Thank you")
elif Num1 == 2:
    print("Well done")
elif Num1 == 3:
    print("Correct")
else:
    print("Error message")

#19-1 변수 제거

Num1 = input("Enter number: ")

while True:
    try:
        Num1 = int(Num1)
        if Num1 == 1:
            print("Thank you")
            break
        elif Num1 == 2:
            print("Well done")
            break
        elif Num1 == 3:
            print("Correct")
            break
        else:
            print("Too high")
            break
    except:
        print("Error message!, Enter a number")
        break
