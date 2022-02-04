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
