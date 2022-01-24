#1.
name = input("Enter your name: ")
print("Hello", name)

#2.
Fname = input("Enter your first name: ")
Lname = input("Enter your last name: ")
print("Hello", Fname, Lname)

#3.
Joke = "What do you call a bear with no teeth?"
answer = "A gummy bear! "

print(Joke + answer)

#3-1
print("What do you call a bear with no teeth?\nA gummy bear! ")

#4
Num1 = input("Enter random number")
Num2 = input("Enter random number2")

print("The total is" Num1 + Num2)

#5
Num1 = input("Enter random number")
Num2 = input("Enter random number2")
Num3 = input("Enter random number3")

print("The answer is " (Num1 + Num2) * Num3)

#6
pizza = input("몇조각으로 시작했니")
pizza1 = input("몇조각 먹었니:")

remain = pizza - pizza1

print(remain)

#7
name = input("Enter your  name: ")
age = input("Enter your age: ")

age = int(age)

print(name, "next birthday you will be", age + 1)

#8
price = input("Enter total price: ")
person = input("Enter How many people: ")

price = int(price)
person = int(person)

print(price / person)

#9
Days = int(input("Enter days: "))
Hours = 24 * Days
min = 60 * Hours
sec = 60 * min
print(Hours, min, sec)


#10

kilo = int(input("Enter kilogram: "))

pound = kilo * 2.204
print(pound)

#11
Num = int(input ("Enter number over 100: "))
Num1 = int(input ("Enter number below 10: "))

print(Num // Num1)
