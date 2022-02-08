#105번
file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Numbers.txt", 'w')
file.write("1,2,3,4,5")
file.close()


#106번
file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Names.txt", 'w')
file.write("유민우\n심은성\n박효신\n전동민\n정지훈\n")
file.close()



#107번
file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Names.txt", 'r')
print(file.read())
file.close()


#108번
file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Names.txt", 'a')
a = input("이름을 입력하세요. : ")
file.write(a + '\n')
file.close()


#109번
print("1) 새파일 만들기\n2) 파일 보기\n3) 새로운 아이템 만들고 출력하기")
a = int(input("1,2 또는 3을 입력하세요. : "))
if a == 1 :
    file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Subject.txt", 'w')
    file.write(input("과목명을 입력하세요. : "))
    file.close()
elif a == 2:
    file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Subject.txt", 'r')
    print(file.read())
    file.close()
elif a == 3:
    file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Subject.txt", 'a')
    file.write('\n' + input("과목명을 입력하세요. : "))
    file.close()
    file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Subject.txt", 'r')
    print(file.read())
    file.close()

else:
    print("잘못된 숫자를 입력했습니다.")



#110번
file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Names.txt", 'r')
print(file.read())
file.close()



file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Names.txt", 'r')
a = input("위 이름들 중 하나를 입력하세요. : ")
a = a + '\n'

for i in file:
    if i != a:
        file = open("C:/Users/MINU/Desktop/MINU/vscode/txtfile/Names2.txt", 'a')
        
        file.write(i)    
        file.close()
file.close()