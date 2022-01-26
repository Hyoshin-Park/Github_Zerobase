# 027

num = float(input('소수점 이하 자릿수가 많은 숫자를 입력하시오: '))
print(num * 2)

# 028

import math

num = float(input('소수점 이하 자릿수가 많은 숫자를 입력하시오: '))
print(round(num * 2, 2))

# 029

import math
num = int(input("500 이상의 정수를 입력하세요.: "))
num2 = math.sqrt(num)
print(round(num2, 2))

# 030

import math
print(round(math.pi, 5))

# 031

import math

num = float(input("원의 반지름을 입력하세요: "))

extent = math.pi * (num ** 2)

print(extent)

# 032

import math

radius = float(input("원의 반지름을 입력하시오: "))
deep = float(input("원의 깊이를 입력하시오: "))
extent = math.pi * (radius ** 2)

volume = extent * deep

print(round(volume, 3))

# 033

num1 = float(input("첫 번째 숫자를 입력하세요.: "))
num2 = float(input("두 번째 숫자를 입력하세요.: "))

num3 = num1 // num2
num4 = num1 % num2

print(num1, "divided by", num2, "is", num3, "with", num4, "remaining")

# 034

import math
print("1) Square")
print("2) Triangle")
print(" ")
print(float(input("Enter a number: ")))

num = float(input("Enter a number: "))

if num == 1:
    one_side = float(input("한 면의 길이를 입력하시오: "))
    square_extent = one_side * one_side
    print(square_extent)

elif num == 2:
    length = float(input("밑변의 길이를 입력하시오: "))
    high = float(input("높이를 입력하시오: "))
    triangle_extent = length * high / 2
    print(triangle_extent)

else:
    print("Error")