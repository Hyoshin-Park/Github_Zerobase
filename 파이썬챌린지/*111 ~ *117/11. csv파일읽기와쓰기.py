import csv
import random

#111
file = open('book.csv','w')
row = 'to -, harper - , 1960\n'
file.write(str(row))
row = 'brief -, ste - , 1988\n'
file.write(str(row))
row = '개츠비 -, 개츠비1 - , 1922\n'
file.write(str(row))
row = '모자, 올리버 - , 1985\n'
file.write(str(row))
row = '오만, 오스틴 - , 1813\n'
file.write(str(row))
file.close()



#112
file.open('book.csv','a')
title = input('제목 : ')
author = input('작가 : ')
year = input('년도 : ')
row = title + ', ' + author + ', ' + year + '\n'
file.write(str(row))
file.close()

file = open('book.csv','r')
for row in file:
    print(row)
file.close()

#113
n = int(input("입력 : "))
file = open('book.csv','a')
for i in range(0, n):
    title = input('제목 : ')
    author = input('작가 : ')
    year = input('년도 : ')
    row = title + ', ' + author + ', ' + year + '\n'
    file.write(str(row))
    file.close()

search = input('입력 : ')
file.open('book.csv','r')
count = 0
for i in file:
    if search in str(i):
        print(i)
        count = count + 1

if count == 0:
    print("없음")
file.close()



#114
start = int(input('입력 : '))
end = int(input('입력 : '))

file = list(csv.reader(open('book.csv')))
list = []
for i in file:
  list.append(i)

for i in list:
  if int(i[2]) >= start and int(i[2]) <= end:
    print(i)




#115
file = open('book.csv','r')
x = 0
for i in file:
  display = 'row : ' + str(x) + ' - ' + i
  print(display)
  x += 1


#116
file = list(csv.reader(open('book.csv')))
list = []
for i in file:
  list.append(i)
  
x = 0
for i in list:
  display = x, list[i]
  print(display)
  x += 1
getrid = int(input('입력 : '))
del list[getrid]

x = 0
for i in list:
  display = x, list[i]
  print(display)
  x += 1
alter = int(input('입력 : '))

x = 0
for i in list:
  display = x, list[alter][i]
  print(display)
  x += 1
part = int(input('입력 : '))
data = input('데이터 입력 : ')
list[alter][part] = data
print(list[alter])

file = open('book.csv','w')
for i in list:
  row = i[0] + ', ' + i[1] + ', ' + i[2] + '\n'
  file.wirte(row)
file.close()






#117
score = 0
name = input('입력 : ')
n1_1 = random.randint(10,50)
n1_2 = random.randint(10,50)
q1 = str(n1_1) + '+' + str(n1_2) + '=' 
a1 = int(input(q1))
r1 = n1_1 + n1_2

if a1 == r1:
  score += 1

n2_1 = random.randint(10,50)
n2_2 = random.randint(10,50)
q2 = str(n2_1) + '+' + str(n2_2) + '=' 
a2 = int(input(q2))
r2 = n2_1 + n2_2
if a2 == r2:
  score += 1


file = open('quizscore.csv','a')
record = name + ', ' + q1 + str(a1) + ', ' + q2 + str(a2) + ', ' + str(score) + '\n'
file.write(str(record))
file.close()