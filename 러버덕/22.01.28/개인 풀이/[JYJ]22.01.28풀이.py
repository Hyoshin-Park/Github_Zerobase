# (Hyo)1.

num1 = int(input('숫자를 입력하세요 : '))
num2 = float(input('숫자를 입력하세요 : '))

plus = num1 + num2
mul = num1 * num2
div = num1 / num2
result = divmod(num1, num2)
print('더하기 : %.2f' % plus)
print('곱하기 : %.2f' % mul)
print('나누기 : %.2f' % div)
print('몫 : %.2f' % result[0])
print('나머지 : %.2f' % result[1])

# (Hyo)2.

num = float(input('점수를 입력하세요 : '))

if num > 1 or num < 0:
    print('Error')

elif num >= 0.9:
    print("A")

elif num >= 0.8:
    print("B")

elif num >= 0.7:
    print("C")

elif num >= 0.6:
    print("D")

elif num < 0.6:
    print("F")


# (Yoo)1.

num1 = float(input('숫자를 입력하세요 : '))
num2 = float(input('숫자를 입력하세요 : '))
div = num1 / num2
print('나누기 : %.2f ' % div)

# (Yoo)2.

num1 = float(input('숫자를 입력하세요 : '))

if num1 > 5:
    print('5보다 크다.')
