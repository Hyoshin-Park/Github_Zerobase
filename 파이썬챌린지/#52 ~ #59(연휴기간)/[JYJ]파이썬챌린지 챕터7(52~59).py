# 052

import random

num = random.randint(1, 100)

print(num)

# 053

import random

fruit = random.choice(['apple', 'banana', 'cherry', 'pear', 'orange'])

print(fruit)


# 054
import random

choice = random.choice(['h', 't'])
question = input('\'h\' 와 \'t\' 중 하나를 고르시오')

if choice == question:
    print('You win')

elif choice != question:
    print('Bad luck')


if question == 'h':
    print('h')

elif choice == 't':
    print('t')

# 055

import random

num = random.randint(1, 5)
choice = int(input('임의의 숫자를 하나 입력하세요'))

if num == choice:
    print('Well done')

elif num > choice:
    print('Too high')
    rechoice = int(input('다시 숫자를 입력하세요'))
    if rechoice == num:
        print('Correct')

    else:
        print('You lose')

elif num < choice:
    print('Too low')
    rechoice = int(input('다시 숫자를 입력하세요'))
    if rechoice == num:
        print('Correct')

    else:
        print('You lose')

# 056

import random

num = random.randint(1, 10)

while True:
    choice = int(input('숫자를 입력하세요 : '))
    if num == choice:
        break

# 057

import random

num = random.randint(1, 10)

while True:
    choice = int(input('숫자를 입력하세요 : '))
    if choice > num:
        print('Too high')
        rechoice = input('다시 숫자를 입력하세요 : ')

    elif choice < num:
        print('Too low')
        rechoice = input('다시 숫자를 입력하세요 : ')

    if num == choice:
        break

# 058

import random

score = 0

for i in range(1, 6):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sum = int(input('{} + {}의 값을 입력하세요'.format(num1, num2)))

    if num1 + num2 == sum:
        score += 1

print(f'맞힌 정답의 개수 : {score}')

# 059

import random

color = random.choice(['red', 'blue', 'green', 'black', 'white'])

while True:
    question = input('red, blue, green, black, white 중 하나의 색을 고르세요')
    if color == question:
        print('Well done')

    else:
        print('You are probably feeling {} right now'.format(question))
        requestion = input('다시 맞혀 보세요')
        if color == requestion:
            break