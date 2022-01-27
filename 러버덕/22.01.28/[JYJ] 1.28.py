# 1. 41의 8 제곱근 구하기 (소수점 둘째 자리 까지만 표시)

# 2. 자신의 키를 입력하여 군면제 대상인지 아닌지 확인해보자(140.0cm 이하 = 면제 대상)

# 3. operator 모듈을 이용하여 13과 7의 합, 곱, 나눗셈을 해보자.(나눗셈은 소수점 셋째 자리 까지 표시)




















# 답 1.

result = 41 ** (1/8)
print('41의 8 제곱근 : %.2f' % result) # 또는

print('41의 8 제곱근 : {}'.format(round(result, 2)))


# 답 2.

height = int(input('키를 입력하세요 : '))
standard = 140

print('군 면제 : {}  '.format(height <= standard))

# 답 3.

import operator

num1 = 13
num2 = 7

print('{} + {} : {}'.format(num1,num2, operator.add(num1, num2)))
print('{} * {} : {}'.format(num1,num2, operator.mul(num1, num2)))
print('{} / {} : {}'.format(num1,num2, round(operator.truediv(num1, num2), 3)))
