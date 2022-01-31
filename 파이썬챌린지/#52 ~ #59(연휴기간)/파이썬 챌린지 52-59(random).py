#52

import random

num = random.randint(1, 100)

print(num)

#53

fruit = random.choice(["cherry", "grape", "apple", "pear", "orange"])

print(fruit)

#54

print("Choose head as in (h) \nor tail as in (t)")
choice1 = input("Your choice is:")

coin = random.choice(["h", "t"])

if choice1 == coin:
    print("You win")
else:
    print("Bad luck")

print(coin)

#55

num = random.randint(1, 5)
numChoice = int(input("Choose a number between 1 and 5: "))
if num == numChoice:
    print("Well done")
elif num > numChoice:
    print("guess a higher number")
    numChoice = int(input("Choose a number between 1 and 5: "))
    if num == numChoice:
        print("Correct")
    else:
        print("You lose")

elif num < numChoice:
    print("guess a smaller number")
    numChoice = int(input("Choose a number between 1 and 5: "))
    if num == numChoice:
        print("Correct")
    else:
        print("You lose")

print(num)

#56

num = random.randint(1, 10)
numChoice = int(input("Choose a number between 1 and 10: "))

while num != numChoice:
    print("Guess a another number")
    numChoice = int(input("Choose a number between 1 and 10: "))

print("Good job")

#57

num = random.randint(1, 10)
numChoice = int(input("Choose a number between 1 and 10: "))

while num != numChoice:
    if num < numChoice:
        print("Guess a smaller number")
    if num > numChoice:
        print("Guess a bigger number")
    numChoice = int(input("Choose a number between 1 and 10: "))

print("Good job")

#58

count = 0

for i in range(0, 5):
    num = random.randint(1, 1000)
    num1 = random.randint(1, 1000)
    addNum = num + num1
    print(f"{num} + {num1} = ?")
    newNum = int(input("Enter your number: "))
    if addNum == newNum:
        count += 1
    else:
        continue
print(count)

#59

print("Red", "Green", "Blue", "White", "Black")

colorChoice = None
color = 0

while colorChoice != color:
    colorChoice = input("Choose a color: ")
    colorChoice = colorChoice.lower()
    color = random.choice(["red", "green", "blue", "white", "black"])

    if colorChoice == color:
        print("Well done")
    else:
        print(f"You look good in {color}")
