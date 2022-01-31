#45

total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total = total + num

print(f"The total is :{total}")

#46

num = int(input("Enter a number: "))

while num < 5:
    num1 = int(input("Enter a new number: "))
    num = num1
print(f"The last number you entered was :{num}")

#47

num = int(input("Enter a number: "))

total = num

add = "y"
while add == "y":
    num2 = int(input("Enter a new number: "))
    total = total + num2
    print("1) add or \n2) do not add")
    add = input("Enter y or n")

print(f"The total is {total}")

# 48

partyPeople = input("Who do you want to invite?: ")

print(f"{partyPeople} has been invited")

count = 1
invite = "y"

while invite == "y":
    print("1) more people enter y or \n2) Its done enter n")
    invite = input("Enter y or n")
    if invite == "y":
        partyPeople = input("who do you want to invite?: ")
        count += 1
    else:
        print(f"You invited {count} people")

#49

compnum = 50

num = int(input("Enter a number: "))

count = 0
while num > compnum or num < compnum:
    if num > compnum:
        print("Guess a small number")
        count += 1
    elif num < compnum:
        print("Guess a bigger number")
        count += 1
    num = int(input("Enter a number: "))

else:
    print(f"Well done, you took {count} attempts")

#50

num = int(input("Enter a number between 10 and 20: "))


while num >= 20 or num <= 10:
    if num >= 20:
        print("Too high")
    elif num <= 10:
        print("Too low")
    num = int(input("Enter a number: "))

else:
    print("Thank you")

#51

num = 10

while num > 0:
    print(f"There are {num} bottles hanging on the wall, \n{num}green bottles hanging on the wall, \nand if 1green bottle should accidently fall ")
    bottle = int(input("how many green bottles will be hanging on the wall?"))
    num -= 1
    while bottle != num:
        print("Try again")
        bottle = int(input("how many green bottles will be hanging on the wall?"))
    if bottle == num:
        print(f"There will be {num} greeen bottles hanging on the wall")




print("There are no more green bottls hanging on the wall")
