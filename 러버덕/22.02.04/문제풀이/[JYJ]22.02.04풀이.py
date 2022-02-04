#[Hyo]

#evenlist = 짝수, oddlist = 홀수, floatlist = 실수
evenList = [] ; oddList = [] ; floatList = []

n = 1
while n < 6:

    try:                              #예외가 발생했을 때
        num = float(input('input number : '))

    except:
        print('예외가 발생했습니다!')
        print('input number again')
        continue

    else:                              #예외가 발생하지 않았을 때
         if num - int(num) != 0:
             print('float number')
             floatList.append(num)

         else:
             if num % 2 == 0:
                 print('even number')
                 evenList.append(num)

             else:
                 print('odd number')
                 oddList.append(num)
    n += 1
print(evenList)
print(oddList)
print(floatList)
############################################

languages = ['C', 'C#', 'java', 'python']
uri = ("C:/Users/jyj/Desktop/R_Prac/python/")

with open(uri + 'duck.txt', 'w') as f:
    f.writelines(languages)

file = open("C:/Users/jyj/Desktop/R_Prac/python/duck.txt", 'r')

str = file.read()
print(str)
file.close

###############################################
#[Yoo]

n1 = input('숫자를 입력하세요 :')
n2 = input('숫자를 입력하세요 :')

try:
    n1 = int(n1)
    n2 = int(n2)

except:
    print('Error')

else:
    print(n1 + n2)

######################