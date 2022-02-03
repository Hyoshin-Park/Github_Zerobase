# 1. lambda 함수를 이용해서 사각형의 넓이를 구해보자.



# 2. import math 모듈을 이용하여 -4.5의 절대값, 올림, 내림 ,버림을 구하여라.



















#풀이 답 1.

width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))

squareArea = lambda n1, n2 : n1 * n2

squareValue = squareArea(width, height)

print(f'사각형의 넓이 : {squareValue}')


# 답2

import math

#절대값
print(math.fabs(-4.5))

#올림
print(math.ceil(-4.5))

#내림
print(math.floor(-4.5))

#버림
print(math.trunc(-4.5))
