#001 사용자의 이름을 입력받아서 다음과 같이 출력하라 Hello[]

name = str(input("사용자의 이름: "))
print("Hello", name)

#002 사용자의 이름을 입력받은 다음, 사용자의 성을 입력받아서 다음과 같이 출력하라.

name = str(input('사용자의 이름: '))
firstname = str(input('사용자의 성: '))
print("Hello", name, firstname)

#003 "What do you call a bear with no teeth?"라는 농담을 표시하고, 다음 줄에 'A gummy bear!'라는 답을 표시하는 코드를 한 줄로 만들자

print("\"What do you call a bear with no teeth\" \n\'A gummy bear!\'")

#004 사용자로부터 2개의 숫자를 입력받아서 더한 결과를 다음과 같이 출력하라

num1 = int(input('첫 번째 숫자: '))
num2 = int(input('두 번째 숫자: '))
result = num1 + num2

print("The total is", result)

#005 사용자로부터 3개의 숫자를 입력받는다. 첫 번째 숫자와 두 번째 숫자를 더한 값에 세 번째 숫자를 곱한 결과를 다음과 같이 출력하라

num1 = int(input('첫 번째 숫자: '))
num2 = int(input('두 번째 숫자: '))
num3 = int(input('세 번째 숫자: '))

result = (num1 + num2) * num3

print("The answer is", result)

# 006 사용자로부터 처음에 가지고 있었던 피자 조각 수를 입력받고, 몇 조각을 먹었는지 입력받아서 남은 조각 수를 계산하여 사람에게 익숙한 형식으로 출력하라

start = int(input('처음에 가지고 있었던 피자 조각 수: '))
eat = int(input('먹은 피자 조각 수: '))
remnant = start - eat

print(start,eat, remnant)

#007 사용자로부터 이름과 나이를 입력받아서 나이에 1을 더한 후 다음과 같이 출력하라.

name = str(input("사용자의 이름: "))
age = int(input("사용자의 나이: "))
next_age = age + 1
print(name, "next birthday you will be", next_age)

#008 계산서의 총 가격과 몇 명이 같이 식사를 했는지 입력받는다. 총 가격을 인원수로 나누고 각 사람이 얼마씩 내야 하는지 출력하라

bill = int(input("계산서의 총 가격: "))
number = int(input("식사 인원"))
each_bill = bill/number

print(each_bill)

#009 사용자로부터 일수(날짜 수)를 입력 받아서 그 일수까지 몇 시간, 몇 분, 몇 초가 남았는지 출력하라.

day = int(input("날짜 수: "))
time = day * 24
minute = time * 60
seconds = minute * 60

print(time,"시간")
print(minute,"분")
print(seconds,"초")

#010 1킬로그램은 2.204파운드다. 몸무게를 킬로그램 단위로 입력받아서 파운드로 변환하여 출력하라.

kg = int(input("몸무게: "))
pound = kg * 2.204

print(pound)

#011 사용자로부터 100이 넘는 숫자를 입력받고 10미만의 숫자 하나를 입력받은 후, 작은 숫자가 큰 숫자 안에 몇 번 들어가는지 사용자 친화적인 형식으로 출력하라.

number1 = int(input("100이 넘는 숫자: "))
number2 = int(input("10미만의 숫자: "))

number3 = number1 // number2

print(number2, "들어간다",number1, number3,"번")
