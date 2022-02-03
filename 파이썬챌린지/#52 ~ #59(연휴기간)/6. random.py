# 6. random

# 완벽한 램덤 값을 만드는 컴퓨터는 없음
# 대신 정확하게 예측할 수 없는 결과를 만든다
# 랜덤값의 2종류
# 1. 특정 범위 내에서의 무작위 값
# 2. 입력된 항목 범위 내에서의 무작위 선택

# random 라이브러리
import random

# 0 ~ 1 사이의 부동소수점 생성
num = random.random()
print(num)
print(num * 100)

# 정수
i_num = random.randint(0, 9)
print(i_num)

#
num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)
newrand = num1 / num2
print(newrand)

# 시작하는 수와 증가 수 주의 (1, 100, 5)
f_num = random.randrange(0, 50, 5)
print(f_num)

#
colour = random.choice(["red","blue","black","green"])
print(colour)


#52
num = random.randint(1, 100)
print(num)


#53
fruits = random.choice(['tomato','banana','peach','blackberry','apple'])
print(fruits)


#54
choice = input("앞/뒤 h/t : ")
ran_choice = random.choice(['h','t'])

if choice == ran_choice:
    print("이김")
else:
    print("짐")
print("컴퓨터 선택 : " + ran_choice)



#55
num = int(input("입력 : "))
ran_num = random.randint(1,5)

if num > ran_num:
    print("더 작게")
elif ran_num > num:
    print("더 크게")

num = int(input("입력 : "))

if num != ran_num:
    print("짐")
else:
    print("정답")


#56
number = random.randint(1, 10)
c_num = int(input('입력 : '))

while number != c_num:
    c_num = int(input('다시 : '))

print('good')


#57
number = random.randint(1, 10)
c_num = int(input('입력 : '))

while number != c_num:
    if number > c_num:
        print('더 크게')
        c_num = int(input('다시 : '))
    else:
        print('더 작게')
        c_num = int(input('다시 : '))
print('good')




#58 문제 이해가 안됨
count = 0
result = 0
while count < 5:
    n1 = random.randint(1, 99)
    n2 = random.randint(1, 99)
    print(n1, '+', n2, ' = ?')
    sum = int(input("입력 : "))
    if sum == n1 + n2:
        count += 1
        result += 1
    else:
        count += 1

print(result, "번 정답")


#59 while 이해필요
print('red, blue, green, black, pink')
c_col = random.choice(['red', 'blue', 'green', 'black', 'pink'])
i_col = input('입력 : ')

while i_col != c_col:
    print(c_col, '위트')
    i_col = input('다시 입력 : ')

print('정답')