#1부터 100까지의 정수 중 7의 배수와 9의 배수를 구분해서 출력하자.(while문 사용)




#2 while문을 이용해서 사용자가 입력한 구구단을 출력하자






















# 1 풀이.
"""
n = 1

while n < 101:
    if n % 7 == 0:
        print('{}은 7의 배수이다.'.format(n))

    elif n % 9 == 0:
        print('{}은 9의 배수이다.'.format(n))

    n += 1

"""



# 2 풀이.

""""

gugu = int(input('출력할 구구단 입력 : '))

n = 1

while n < 10:
    result = gugu * n
    print(f'{gugu} * {n} = {result}')
    n += 1
    
"""