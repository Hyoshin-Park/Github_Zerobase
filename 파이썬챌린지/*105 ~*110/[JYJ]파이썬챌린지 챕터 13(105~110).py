# 105

file = open('C:/Users/jyj/Desktop/R_Prac/python/Numbers.txt', 'w')
file.write('1, ')
file.write('2, ')
file.write('3, ')
file.write('4, ')
file.write('5')
file.close()

# 106

file = open('C:/Users/jyj/Desktop/R_Prac/python/Names.txt', 'w')
file.write('김범수\n')
file.write('나얼\n')
file.write('박효신\n')
file.write('이수\n')
file.write('윤종신\n')
file.close()

# 107

file = open('C:/Users/jyj/Desktop/R_Prac/python/Names.txt', 'r')
names = file.read()
print(names)
file.close()

# 108

file = open('C:/Users/jyj/Desktop/R_Prac/python/Names.txt', 'a')
new_name = input('새로운 이름을 입력하세요 : ')
file.write(new_name + '\n')
file.close()

file = open('C:/Users/jyj/Desktop/R_Prac/python/Names.txt', 'r')
new_name = file.read()
print(new_name)
file.close()

# 109

print('1) Creat a new file' + '\n' + '2) Disply the file' + '\n' + '3) Add a new item to the file')
choice = int(input('1,2 또는 3을 입력하세요 : '))

if choice == 1:
    subject = input('과목명을 입력하세요 : ')
    file = open('C:/Users/jyj/Desktop/R_Prac/python/Subject.txt', 'w')
    file.write(subject + '\n')
    file.close()

elif choice == 2:
    file = open('C:/Users/jyj/Desktop/R_Prac/python/Subject.txt', 'r')
    file.read()
    print(file.read())
    file.close()

elif choice == 3:
    new_subject = input('새로운 과목명을 입력하세요 : ')
    file = open('C:/Users/jyj/Desktop/R_Prac/python/Subject.txt', 'a')
    file.write(new_subject + '\n')
    file = open('C:/Users/jyj/Desktop/R_Prac/python/Subject.txt', 'r')
    print(file.read())
    file.close()

else:
    print('error')

# 110

file = open('C:/Users/jyj/Desktop/R_Prac/python/Names.txt', 'r')
new_name = file.read()
print(new_name)
file.close()

file = open('C:/Users/jyj/Desktop/R_Prac/python/Names.txt', 'r')
choice = input('하나의 이름을 입력하세요 : ')
choice = choice + '\n'

for i in file:
    if i != choice:
        file = open('C:/Users/jyj/Desktop/R_Prac/python/Names.txt', 'a')
        file.write(i)
        file.close()
file.close()