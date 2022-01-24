#1번
#사용자의 이름을 입력받아서 다음과 같이 출력하라.
#Hello[이름]

name = input("이름을 입력하세요.  ")

print("Hello", name)


#2번
# 사용자의 이름을 입력받은 다음, 사용자의 성을 입력받아서 다음과 같이 출력하라.
# Hello [이름] [성]

name1 = input("성을 입력하세요.  ")
name2 = input("이름을 입력하세요.  ")

print("Hello", name2, name1)


#3번
#'What do you call a bear with no teeth?'라는 농담을 표시하고,
#다음 줄에 'A gummy bear!'라는 답을 표시하는 코드를 한 줄로 만들자.

print("What do you call a bear with no teeth?\nA gummy bear!")


#4번
#사용자로부터 2개의 숫자를 입력받아서 더한 결과를 다음과 같이 출력하라.
#The total is [결과]

num1 = int(input("숫자를 입력하세요. "))
num2 = int(input("숫자를 입력하세요. "))

ans = num1 + num2

print("The total is", ans)


#5번
#사용자로부터 3개의 숫자를 입력받는다. 첫 번째 숫자와 두 번째 숫자를 더한 값에 
#세 번째 숫자를 곱한 결과를 다음과 같이 출력하라.
#The answer is [결과]

num1 = int(input("숫자를 입력하세요. "))
num2 = int(input("숫자를 입력하세요. "))
num3 = int(input("숫자를 입력하세요. "))

sum = num1 + num2
ans = sum * num3

print("The answer is", ans)


#6번
#사용자로부터 처음에 가지고 있었던 피자 조각 수를 입력받고, 몇 조각을 먹었는지
#입력받아서 남은 조각수를 계산하여 사람에게 익숙한 형식으로 출력하라.


first = int(input("처음에 가지고 있었던 피자의 조각 수는? : "))
last = int(input("먹은 피자의 조각 수는? : "))

pizza = first - last
print(f"피자가 {pizza}조각 남았습니다.")


#7번
#사용자로부터 이름과 나이를 입력받아서 나이에 1을 더한 후 다음과 같이 출력하라.
#[이름] next birthday you will be [새로운 나이]

name = input("이름은 무엇입니까? : ")
age = int(input("몇 살입니까? : "))
new_age = age + 1

print(f"{name} next birthday you will be {new_age}")



#8번
#계산서의 총 가격과 몇 명이 같이 식사를 했는지 입력받는다.
#총 가격을 인원수로 나누고 각 사람이 얼마씩 내야하는지 출력하라.

total = int(input("계산서의 총 가격 : "))
people = int(input("몇 명이서 먹었나요? : "))

price = total / people
print(f"한 명씩 {price}원을 내야합니다.")


#9번
#사용자로부터 일수(날짜 수)를 입력받아서 그 일수를 시간, 분, 초로 환산하라.

days = int(input("일수를 입력하세요. : "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"{days}일은 시간으로 {hours}시간, 분으로 {minutes}분, 초로 {seconds}초이다.")


#10번
#1킬로그램은 2.204파운드다.
#몸무게를 킬로그램 단위로 입력받아서 파운드로 변화하여 출력하라.

weight = float(input("몸무게를 입력하세요.(kg) : "))
lb = round(weight * 2.204623, 2)
print(f"당신의 몸무게를 파운드로 환산하면 {lb}lb입니다.")


#11번
#사용자로부터 100이 넘는 숫자를 입력받고 10 미만의 숫자 하나를 입력받은 후, 
#작은 숫자가 큰 숫자 안에 몇 번 들어가는지 사용자 친화적인 형식으로 출력하라.

large = int(input("100이 넘는 숫자를 입력하세요. : "))
small = int(input("10미만의 숫자를 입력하세요. : "))

x = large // small

if (small == 1 or small == 3 or small == 6 or small == 7 or small == 8):
    print(f"{small}은 {large}안에 {x}번 들어갑니다.")
else:
    print(f"{small}는 {large}안에 {x}번 들어갑니다.")