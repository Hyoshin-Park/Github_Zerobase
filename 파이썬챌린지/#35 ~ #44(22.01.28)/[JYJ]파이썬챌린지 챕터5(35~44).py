# 035

name = input('사용자의 이름을 입력하시오 : ')

for i in range(1, 4):
    print(name)

# 036

name = input('사용자의 이름을 입력하시오 : ')
num = int(input('숫자를 입력하시오 : '))

for i in range(0, num):
    print(name)

# 037

name = input('이름을 입력하세요 : ')

for i in name:
    print(i)

# 038

name = input('이름을 입력하세요 : ')
num = int(input('숫자를 입력하세요 : '))

for a in range(0, num):
    for i in name:
        print(i)

# 039

num = int(input('1~12 사이의 값을 입력하세요 : '))

for i in range(1, 13):
    multiply = i * num
    print(i, num , multiply)

# 040

num = int(input('50 미만의 숫자를 입력하세요 : '))

for i in range(50, num - 1, -1):
    print(i)

# 041

name = input('이름을 입력하세요 : ')
num = int(input('숫자를 입력하세요 '))

if num < 10:
    for i in range(0, num):
        print(name)

else:
    for o in range(0, 3):
        print("Too high")

# 042

total = 0

for i in range(0, 5):
    num = int(input('숫자를 입력하세요 : '))
    plus = int(input('입력한 값을 더 할 것인가? 1. yes 2. no'))
    if plus == 1:
        total += num

print(total)

# 043

want = int(input('원하는 카운트 방향을 고르시오 1. 카운트 다운 2. 카운트 업'))

if want == 1:
    big = int(input('가장 큰 숫자를 적으시오 : '))
    for i in range(1, big + 1):
        print(i)

elif want == 2:
    small = int(input('20미만의 숫자를 적으시오 :'))
    for o in range(20, small - 1, -1):
        print(o)

else:
    print('I don\'t understand')

# 044

num = int(input('파티에 몇 명을 초대하고 싶습니까? :'))

if num < 10:
    for i in range(0, num):
        name = input('이름이 무엇입니까?')
        print(name, "has been invited")

else:
    print("Too many people")