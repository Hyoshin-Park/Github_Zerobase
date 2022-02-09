#111

import csv

file = open("Books.csv", "w")

file.write("To Kill A Mockingbird " + "," +"Harper Lee" + "," + "1960\n")
newRecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newRecord))
newRecord = "The Great Gastby, F.Scott Fitzgerald, 1922\n"
file.write(str(newRecord))
newRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newRecord))
newRecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newRecord))
file.close()

#112

import csv

file = open("Books.csv", "a")

record = input("Add Record")

file.write(str(record))
file.close()

file = open("Books.csv", "r")

for i in file:
    print(i)

file.close()


#113

import csv

file = open("Books.csv", "a")

askRecord = int(input("How many to add?: "))

for l in range(askRecord):
    title = input("Enter title: ")
    Author = input("Enter Author: ")
    year = input("Enter year: ")
    record = title + "," + Author + "," + year + "\n"
    file.write(str(record))
file.close()

askWho = input("Who do you want to search?: ")

file = open("Books.csv", "r")

count = 0

for i in file:
    if askWho in str(i):
        print(i)
        count += 1
if count == 0:
    print("Not in csv.!")

file.close()


#114

import csv

file = list(csv.reader(open("Books.csv")))

start = int(input('Enter starting year: '))
end = int(input('Enter ending year: '))

list = []
for l in file:
    list.append(l)

for l in list:
     if int(l[2]) >= start and int(l[2]) <= end:
         print(l)

file.close()



#115

import csv

file = list(csv.reader(open("Books.csv")))

row = list(file)

for i in range(0, len(row)):
     print(f"number is {i} and data is {row[i]}")


#116

import csv



file = list(csv.reader(open("Books.csv")))

row = list(file)

print(row)

askInput = int(input("Which row do you want to delete?: "))

del row[askInput]

askInput1 = int(input("Which row do you want to change?: "))
change = input("How do you want to change?: ")

row[askInput1] = change


file = open("Books.csv", "w")

for new in row:
    newC = new[0] + "," + new[1] + "," + new[2] + "\n"
    file.write(newC)

file.close()


#117

import csv

import random

name = input("Your name?: ")

answerResult = 0

num1 = random.randint(1, 11)
num2 = random.randint(1, 11)
quiz = str(num1) + "*" + str(num2) + "="
result = num1 * num2

QUESTION = int(input(quiz))
if result == QUESTION:
        answerResult += 1

num3 = random.randint(1, 11)
num4 = random.randint(1, 11)
quiz1 = str(num3) + "*" + str(num4) + "="
result1 = num3 * num4

QUESTION1 = int(input(quiz ))
if result1 == QUESTION1:
        answerResult += 1


InCsv = name + "," + quiz + "," + str(result) + ","
+ "," + quiz1 + "," + str(result1) + "," + str(answerResult) + "\n"

file = open("Math QUESTION.csv", "a")

file.write(InCsv)

file.close()
