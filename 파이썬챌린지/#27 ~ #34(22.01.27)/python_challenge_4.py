# 0127
# 수학함수

import math
# 27 : 사용자에게 소수점 이하 자릿수가 많은 숫자를 입력하도록 요청한다 이 숫자에 2를 곱한 결과를 출력하라
# input함수는 str
number = float(input("입력 : "))
print(number * 2)

# 28 : 27번 프로그램을 업데이트하여 소수점 둘째 자리까지 출력하라
number = float(input("입력 : "))
print(round(number * 2, 2))


# 29 : 사용자에게 500 이상의 점수를 입력하라고 요청한다 입력받은 숫자의 제곱근을 구하고 소수점 둘째 자리까지 출력하라
number = int(input("500 이상 입력 : "))
print(round(math.sqrt(number), 2))


# 30 : 파이값을 소수점 다섯째 자리까지 출력하라
print("파이",math.pi)
print("파이",round(math.pi, 5))

# 31 : 사용자에게 원의 반지름을 입력하도록 요청한다 원의 넓이를 계산하여 출력하라
radius = int(input("입력 : "))
print(radius * radius * 3.14)

# 32 : 원기둥의 반지름과 깊이를 입력하도록 요청한다 원기둥의 부피(원 넓이*깊이)를 구하고 결과를 반올림하여 소수점 세째 자리까지 출력하라
radius = float(input("원기둥 반지름 입력 : "))
height = float(input("원기둥 깊이 입력 : "))
print("원기둥 부피 : ", round(radius * height, 3))

# 33:사용자로부터 숫자 두 개를 입력받는다. 몫 연산을 사용하여 첫 번째 숫자를 두 번째 숫자로 나누고 나머지도 계산하여 사용자가 읽을 수 있는 문장으로 결과를 출력하라
num1 = int(input("1 입력 : "))
num2 = int(input("2 입력 : "))
q = num2 // num1
r = num2 % num1
print("몫은 ", q, "이고 나머지는 ", r, "이다")

# 34 : 다음과 같은 메시지를 표시한다 1)Square 2)Triangle Enter a number : 만약 사용자가 1을 입력하면 한 변의 길이를 요청하여 사각형의 넓이를 구하여 출력하라 만약 2를 입력하면 밑변과 높이를 요청하여 삼각형의 넓이를 구하여 출력하라 다른 것을 입력하면 적절한 오류 메시지가 출력되도록 하라
print("1) 사각형")
print("1) 삼각형")
number = int(input("입력 : "))

if number == 1:
  number = int(input("길이 : "))
  print("사각형의 넓이 : ", number * number)
elif number == 2:
  num1 = int(input("밑변 : "))
  num2 = int(input("높이 : "))
  print("삼각형의 넓이 : ", (num1 * num2) / 2)
else:
  print("입력 오류")