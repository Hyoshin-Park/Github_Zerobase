import csv
# 111번

file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","w")
a = "To Kill A Mockingbird, Harper Lee, 1960\nA Brief History of Time, Stephen Hawking, 1988\nThe Great Gatsby, F. Scott Fitzgerald, 1922\nThe Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\nPride and Prejudice, Jane Austen, 1813\n"

file.write(a)
file.close()


#112번
file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","a")

title = input("제목 : ")
author = input("저자 : ")
year = input("출간연도 : ")

new = title + ',' + author + ',' + year + '\n'

file.write(new)
file.close()



#113번
file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","a")

num = int(input("몇 개를 추가하고 싶으세요? : "))
for i in range(num):
    title = input("제목 : ")
    author = input("저자 : ")
    year = input("출간연도 : ")

    new = str(title + ',' + author + ',' + year + '\n')

    file.write(new)
file.close()
file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","r")

name = input("검색할 저자의 이름을 입력하세요. : ")
c = 0
for j in file:
    if name in j:
        print(str(j))
        c+=1

if c == 0:
    print("검색하신 저자의 책이 없습니다.")
file.close()



#114번
file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","r")

year1 = int(input("시작 년도를 입력하세요. : "))
year2 = int(input("끝 년도를 입력하세요. : "))

a = csv.reader(file)
r = list(a)
for i in r:
    if year1 < int(i[2]) < year2:
        print(i)
file.close()



#115번
file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","r")

for idx, i in enumerate(file):
    print(f"{idx}행 : {i}")
file.close()



#116번
file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","r")
new = []

a = list(csv.reader(file))


for idx, i in enumerate(a):
    new.append(i)
    print(idx,i)
num = int(input("삭제하고 싶은 행을 입력하세요. : "))
del new[num]

for id, j in enumerate(new):
    print(id,j)

num1 = int(input("수정하고 싶은 데이터를 선택하세요. : "))
del new[num1]

title = input("제목 : ")
author = input("저자 : ")
year = input("출간연도 : ")

bbb = [title]+[author]+[year]

new.insert(num1,bbb)

file.close()
file = open("C:/Users/Yoo/Desktop/MINU/Coding/Books.csv","w")
for m in new:
    asd = m[0]+','+m[1]+','+m[2]+'\n'
    file.write(asd)
file.close()


#117번
import random
name = input("이름이 뭐죠 : ")
num1 = random.randint(1,11)
num2 = random.randint(1,11)
Q1 = num1+num2
q1 = str(num1) + '+' + str(num2)
a1 = input(f"{q1} : ")
Q2 = num1*num2
q2 = str(num1) + '*' + str(num2)
a2 = input(f"{q2} : ")

if Q1 == int(a1) and Q2 == int(a2):
    cnt = 2
elif Q1 != int(a1) and Q2 != int(a2):
    cnt = 0
else:
    cnt = 1


file = open("C:/Users/Yoo/Desktop/MINU/Coding/add.csv","a")

co = name + ',' + q1 + ',' + a1 + ',' + q2 + ',' + a2 + ',' + str(cnt) +'\n'
file.write(co)
file.close()