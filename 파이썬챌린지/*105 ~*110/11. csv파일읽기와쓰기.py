#


#105 파일 있는 폴더에 만들어짐
file = open('numbers.txt','w')
file.write('0,')
file.write('1,')
file.write('2,')
file.write('3,')
file.write('4,')
file.close()

#106
file1 = open('name.txt','w')
file1.write('kim\n')
file1.write('lee\n')
file1.write('im\n')
file1.write('han\n')
file1.write('yong\n')
file1.close()


#107
file2 = open('name.txt','r')
print(file2.read())
file2.close()


#108
file3 = open('name.txt','a')
name = input('입력 : ')
file3.write(name + '\n')
file3.close()

file8 = open('name.txt','r')
print(file.read())
file.close()


#109
print('1, 새파일만들기')
print('2. 파일열기')
print('3. 추가하기')
num = input('입력 : ')
if num == '1':
    sub = input('과목명 입력 : ')
    file4 = open('subject.txt','w')
    file4.write(sub + '\n')
    file4.close()
elif num == '2':
    file4 = open('subject.txt','r')
    print(file4.read())
else:
    sub = input('과목명 입력 : ')
    file4 = open('subject.txt', 'a')
    file4.write(sub + '\n')
    file4.close()
    file4 = open('subject.txt', 'r')
    print(file4.read())




#110

file5 = open('name.txt','r')
print(file5.read())
file5.close()

name = input('이름입력 : ')
name = name + '\n'

file5 = open('name.txt','r')

for row in file5:
    if row != name:
        file = open('name2.txt', 'a')
        file.write(row)
        file.close()

file5.close()