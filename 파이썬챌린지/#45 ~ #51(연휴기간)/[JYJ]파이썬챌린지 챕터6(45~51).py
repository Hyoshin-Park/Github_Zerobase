# 045

total = 0

while total <= 50:
    num = int(input('숫자를 입력하세요 : '))
    total += num
    print(f'The total is {total}')


# 046

num = 0

while num <= 5:
    num = int(input('숫자를 입력하세요 : '))
    print('The last number you entered was a {}'.format(num))

# 047

num1 = int(input('숫자를 입력하세요 : '))
total = num1
flag = True

while flag:
    num2 = int(input('숫자를 입력하세요 : '))
    total += num2
    question = input('또 다른 숫자를 더하시겠습니까? : (y / n)')
    if question == 'n':
        break

print(total)

# 048

flag = True
count = 0
while flag:
    name = input('초대하고 싶은 사람의 이름을 입력하세요 : ')
    print(f'{name} has now been invited')
    count += 1
    question = input('다른 사람을 더 초대하고 싶습니까? (y/n)')

    if question == 'n':
        break

print(count)

# 049

compnum = 50

num = int(input('숫자를 입력하세요 : '))

count = 1

while num != compnum:

    if num > compnum:
        print('Too high, 다시 맞춰 보세요')

    elif num < compnum:
        print('Too low. 다시 맞춰 보세요')

    elif num == compnum:
        break

    count += 1
    num = int(input('다시 입력하세요 : '))

print(count)

# 050

num = int(input('숫자를 입력하세요 : '))

while num < 10 or num > 20:
    if num <= 10:
        print('Too low, 다시 입력하세요.')

    elif num >= 20:
        print('Too high, 다시 입력하세요.')


    num = int(input('다시 입력해 주세요.'))

print('Thank you')


# 051

num = 10

while num > 0:

    print('There are {} green bottles hanging on the wall, {} green bottles hanging on the wall, and if 1 green bottle should accidentally fall'.format(num, num))
    answer = int(input('How many green bottles will be hanging on the wall? : '))
    num -= 1

    if answer == num:
        print(f'There will be {answer} green bottles hanging on the wall')

    elif answer != num:
        answer = int(input('No, try again : '))

print('There are no more green bottles hanging on the wall')
