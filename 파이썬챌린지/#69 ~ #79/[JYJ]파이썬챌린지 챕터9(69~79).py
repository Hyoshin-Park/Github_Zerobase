# 069

country = ('Korea', 'Japan', 'Canada', 'USA', 'Indo')
print(country)
choice = input('표시된 국가 이름들 중 하나를 입력하라 : ')
print(country.index(choice))

# 070

country = ('Korea', 'Japan', 'Canada', 'USA', 'Indo')
print(country)
choice = input('표시된 국가 이름들 중 하나를 입력하라 : ')
print(country.index(choice))

num = int(input('0 ~ 4 까지의 숫자를 입력하세요.'))
print(country[num])

# 071

sports = ['soccer', 'baseball']

sports.append(input('좋아하는 스포츠가 무엇인가요? '))
sports.sort()
print(sports)

# 072

subject_list = ['math', 'kor', 'eng', 'his', 'sci', 'phy']
print(subject_list)

hate = input('좋아하지 않는 과목이 무엇입니까? : ')

num = subject_list.index(hate)

del subject_list[num]

print(subject_list)

# 073

food = {}

for i in range(1, 5):
    food[i] = input('좋아하는 음식 네 개를 입력하세요 : ')

print(food)

hate = int(input('제거 하고 싶은 항목이 있나요? : '))

del food[hate]

print(food)

# 074

color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'gray', 'white', 'black']
start = int(input('0에서 4 사이의 값을 입력하세요 :'))
end = int(input('5에서 9 사이의 값을 입력하세요 :'))

print(color[start:end])

# 075

num_list = [123, 456 ,789 ,101]

for i in num_list:
    print(i)

num = int(input('세 자리 숫자를 입력하세요 : '))

if num in num_list:
    print(num_list.index(num))

else:
    print('That is not in the list')

# 076

name = []

for i in range(0, 3):
    name.append(input('파티에 초대할 사람의 이름을 입력하세요?'))

while True:
    more = input('더 추가할 사람이 있습니까? y/n ')
    if more == 'y':
        name.append(input('추가할 사람을 적어주세요'))
    else:
        print(len(name))
        break

# 077

name = []

for i in range(0, 3):
    name.append(input('파티에 초대할 사람의 이름을 입력하세요?'))

while True:
    more = input('더 추가할 사람이 있습니까? y/n ')
    if more == 'y':
        name.append(input('추가할 사람을 적어주세요'))
    else:
        print(len(name))
        break
print(name)

choice = input('리스트에 있는 이름들 중 하나를 입력하세요 : ')
print(name.index(choice))

real = input('{}님을 정말로 초대 하시겠습니까? y/n'.format(choice))

if real == 'n':
    name.remove(choice)
    print(name)
else:
    print(name)

# 078

tv = ['무한도전', '1박2일', '런닝맨', '신서유기']

for i in tv:
    print(i)

tv_want = input('원하는 프로그램을 입력하세요 : ')
tv_where = int(input('몇 번째 인덱스에 추가하고 싶으세요'))

tv.insert(tv_where, tv_want)
for i in tv:
    print(i)

# 079

nums = []

for i in range(0, 3):
    num = int(input('숫자를 입력하세요 : '))
    nums.append(num)
print(nums)

question = input('마지막 숫자를 저장 하시겠습니까? y/n')

if question == 'n':
    nums.remove(3)
    print(nums)

else:
    print(nums)