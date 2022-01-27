## 27

# num = float(input("소수점 이하 자릿수가 많은 숫자를 입력하세요. : "))
# print(num*2)



##28

# num = float(input("소수점 이하 자릿수가 많은 숫자를 입력하세요. : "))
# print(round(num*2,2))



##29

# import math
# num = float(input("500 이상의 정수를 입력하세요. : "))
# numnum = math.sqrt(num)
# print(round(numnum, 2))


##30

# import math
# print(round(math.pi, 5))


##31

# import math
# r = int(input("원의 반지름 길이를 입력하세요. : "))

# print(math.pi * (r**2))



##32

# import math
# r = int(input("원기둥의 반지름 길이를 입력하세요. : "))
# h = int(input("원기둥의 높이를 입력하세요. : "))

# print(math.pi * (r**2) * h)



##33

# num1 = int(input("첫번째 숫자를 입력하세요. : "))
# num2 = int(input("두번째 숫자를 입력하세요. : "))

# quotient = num1//num2
# remainder = num1%num2

# print(f"{num1}을 {num2}로 나눴을 때 몫은 {quotient}이고, 나머지는 {remainder}이다.")



##34

# print("1) 정사각형")
# print("2) 삼각형")

# num = int(input("숫자를 입력하세요. : "))

# if num == 1:
#     length = int(input("한 면의 길이를 입력하세요 : "))
#     print(f"정사각형의 넓이는 {length**2}입니다.")
# elif num ==2:
#     bottom = int(input("밑변의 길이를 입력하세요 : "))
#     height = int(input("높이를 입력하세요 : "))
#     print(f"삼각형의 넓이는 {bottom * height /2 }입니다.")
# else:
#     print("1 또는 2를 입력하세요.")