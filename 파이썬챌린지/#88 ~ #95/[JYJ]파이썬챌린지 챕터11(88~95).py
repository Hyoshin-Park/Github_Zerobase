# 080

firstname = input('이름이 어떻게 되시나요?: ')
print(len(firstname))
lastname = input('성이 어떻게 되시나요?: ')
print(len(lastname))

name = lastname + " " + firstname
print(name)
print(len(name))

# 081

subject = input('가장 좋아하는 과목이 무엇입니까?: ')
for i in subject:
    print(i, end = "-")

# 082

poem = 'we victory'
print(poem)
start = int(input('시작 인덱스를 입력하세요 : '))
end = int(input('마지막 인덱스를 입력하세요 : '))

print(poem[start:end])

# 083

message = input('대문자로 메시지를 입력하세요')

while True:

    if message.isupper() == False:
        print('Try again')
        message = input('메세지를 다시 입력하세요')

    elif message.isupper() == True:
        print('Good!')
        break

# 084

word = input('영어 단어를 입력하세요')

start = word[0:2]

print(start.upper())

# 085

name = input('이름을 입력하세요: ')
count = 0

for i in name:
    if i == "a" or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1

print(count)

# 086

newPassword = input('새로운 비밀번호를 입력하세요 : ')
rePassword = input('한번 더 입력하세요 : ')

if newPassword == rePassword:
    print('Thank you')

elif newPassword.islower != rePassword.islower:
    print('They must  be in the same case')

else:
    print('Incorrect')

# 087

word = input('단어를 입력하세요 : ')
reverse = ''
for i in word[::-1]:
    print(i)

# 088

from array import *

nums = array('i', [])

for i in range(0, 5):
    num = int(input('숫자를 입력하세요 : '))
    nums.append(num)

nums = sorted(nums)
nums.reverse()
print(nums)

# 089

from array import*
import random

nums = array('i', [])

for i in range(0, 5):
    num = random.randint(0, 100)
    nums.append(num)

for i in nums:
    print(i)

# 090

from array import *

nums = array('i', [])

n = 0

while n < 5:
    num = int(input('숫자를 입력하세요 : '))
    if num >= 10 and num < 20:
        nums.append(num)
        n += 1

    else:
        print('Outside the range')

print('Thank you')

for i in nums:
    print(i)

# 091

from array import *

nums = array('i', [2, 3, 5, 5, 7, 9])
print(nums)

question = int(input('배열에 있는 숫자들 중 하나를 입력하세요 : '))

print(f'입력한 숫자가 리스트에 {nums.count(question)}개 있습니다.')

# 092

from array import *
import random

num1 = array('i', []) # 사용자가 입력할 3개의 숫자
num2 = array('i', []) # 다섯개의 임의의 숫자

for i in range(0, 3):
    a = int(input('숫자를 입력해 주세요 : '))
    num1.append(a)


for x in range(0, 5):
    b = random.randint(1, 100)
    num2.append(b)

num1.extend(num2)
num1 = sorted(num1)
for y in num1:
    print(y)

# 093

from array import *

num = array('i', [])


for i in range(0, 5):
    a = int(input('숫자를 입력하세요 : '))
    num.append(a)

for i in num:
    print(i)

num = sorted(num)
request = int(input('배열의 숫자들 중 하나를 고르시오 : '))

num2 = array('i', [])

num1 = num.remove(request)


num2.append(request)

for i in num2:
    print(i)


# 094
from array import *

num1 = array('i', [12, 24, 36, 48, 60])
print(num1)
select = int(input('다음 숫자들 중 하나를 골라주세요'))
flag = True

while flag:
    if select in num1:
        print(num1.index(select))
        flag = False
    else:
        print(input('다시 입력하세요'))

# 095

from array import *

num1 = array('f', [35.74, 39.85, 88.12, 45.63, 66.12])

question = int(input('2와 5사이의 정수를 입력하세요 : '))

flag = True

while flag:
    if question < 2 or question > 5:
        print(int(input('Error \n다시 입력하세요.')))

    else:
        for i in num1:
            print(round(i / question, 2))
        break