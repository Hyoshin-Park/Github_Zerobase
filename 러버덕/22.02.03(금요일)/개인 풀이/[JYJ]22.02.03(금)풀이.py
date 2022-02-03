# [Yoo] 1.

n = int(input('숫자를 입력하세요 : '))

for i in range(1, 10):
    print(f'{n} * {i} = {n*i}')

# [Yoo] 2.

n = int(input('숫자를 입력하세요 : '))
a = 1
while a <= n:
    print(a)
    a += 1

# [Hyo]

print('-' * 25)
print('1. 아메리카노, 2. 카페라떼, 3. 카라멜마끼야또, 4. 자몽에이드, 5. 유자차')
select = int(input('메뉴 번호를 입력해주세요 : '))
if select == 1:
    print('아메리카노 가격  = 2500원')

elif select == 2:
    print('카페라떼 가격 = 3000원')

elif select == 3:
    print('카라멜마끼야또 가격 = 3000원')

elif select == 4:
    print('자몽에이드 가격 = 4500원')

elif select == 5:
    print('유자차 가격 = 4000원')

else:
    print('잘못된 메뉴입니다.')
print('-' * 25)