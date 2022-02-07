# 096

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)

# 097

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)
a = int(input('행을 선택하세요 : '))
b = int(input('열을 선택하세요 : '))

print(list[a][b])

# 098

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)

a = int(input('출력할 행을 입력해주세요 : '))
print(list[a])

b = int(input('출력한 행에 추가 할 값을 입력해주세요 : '))

list[a].append(b)
print(list[a])

# 099

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)

row = int(input('어떤 행을 출력하시겠습니까? : '))
print(list[row])

col = int(input('어떤 열을 출력하시겠습니까? : '))
print(list[row][col])

change = input('그 값을 변경하고 싶습니까? y/n ')

if change == 'y':
    new = int(input('새로운 값을 입력하세요 : '))
    list[row][col] = new

print(list)

# 100

data = {'John' : {'N' : 3056, 'S' : 8463, 'E' : 8441, 'W' : 2694},
        'Tom' : {'N' : 4832, 'S' : 6786, 'E' : 4737, 'W' : 3612},
        'Anne' : {'N' : 5239, 'S' : 4802, 'E' : 5820, 'W' : 1859},
        'Fiona' : {'N' : 3904, 'S' : 3645, 'E' : 8821, 'W' : 2451}}

print(data)

# 101

data = {'John' : {'N' : 3056, 'S' : 8463, 'E' : 8441, 'W' : 2694},
        'Tom' : {'N' : 4832, 'S' : 6786, 'E' : 4737, 'W' : 3612},
        'Anne' : {'N' : 5239, 'S' : 4802, 'E' : 5820, 'W' : 1859},
        'Fiona' : {'N' : 3904, 'S' : 3645, 'E' : 8821, 'W' : 2451}}

print(data)

name = input('사용자의 이름을 입력하세요 : ')
area = input('사용자의 지역을 입력하세요 : ')

print(data[name][area])

change = int(input('이름과 지역의 변경하려는 데이터를 입력하세요 : '))

data[name][area] = change

print(data[name])

# 102

from array import *

list = {}

for i in range(0, 4):
    name = input('이름을 입력하세요 : ')
    age = int(input('나이를 입력하세요 : '))
    size = int(input('신발 사이즈를 입력하세요 : '))
    list[name] = {"Age" : age, "Size" : size}

print(list)

request = input('이름을 입력하세요 : ')

print(list[request])

# 103

list = {}

for i in range(0, 4):
    name = input('이름을 입력하세요 : ')
    age = int(input('나이를 입력하세요 : '))
    size = int(input('신발 사이즈를 입력하세요 : '))
    list[name] = {"Age" : age, "Size" : size}


# del list[name] < key는 삭제가 되는데
# del list["Age"] < value는 삭제가 안되는듯? 그래서 오류가 생긴거 같음
# print(list)

for i in list:
    print(i, list[name]['Age'])

# 104

list = {}

for i in range(0, 4):
    name = input('이름을 입력하세요 : ')
    age = int(input('나이를 입력하세요 : '))
    size = int(input('신발 사이즈를 입력하세요 : '))
    list[name] = {"Age" : age, "Size" : size}

eli = input('목록에서 제거하고 싶은 사람의 이름을 입력하세요 : ')

del list[eli]

for i in list:
    print(i, list[name]["Age"], list[name]["Size"])
