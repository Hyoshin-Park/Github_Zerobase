# 10. 2차원 리스트와 딕셔너리


#96
"""list = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
print(list)
"""
#97
list = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
row = int(input('선택 : '))
col = int(input('선택 : '))
print(list[row][col])


#98
list = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
row = int(input('입력 : '))
print(list[row])

new = int(input('입력 : '))
list[row].append(new)
print(list[row])


#99
list = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
row = int(input('입력 : '))
print(list[row])

col = int(input('컬럼 입력 : '))
print(list[row])

cha = input("y/n")
if cha == 'y':
    new = col = int(input('컬럼 입력 : '))
    list[row][col] = new
print(list)

#100
sales = {
    "john":{"n":3056, "s":8463, "e":8441, 'w':2694},
    "tom":{"n":4832, "s":6786, "e":4737, 'w':3612},
    "anne":{"n":5239, "s":4802, "e":5820, 'w':1859},
    "fiona":{"n":3904, "s":3645, "e":8821, 'w':2451},
}

#101
sales = {
    "john":{"n":3056, "s":8463, "e":8441, 'w':2694},
    "tom":{"n":4832, "s":6786, "e":4737, 'w':3612},
    "anne":{"n":5239, "s":4802, "e":5820, 'w':1859},
    "fiona":{"n":3904, "s":3645, "e":8821, 'w':2451},
}
name = input('이름 : ')
region  = input('지역 : ')
print(sales[name][region])
new = int(input("입력 : "))
sales[name][region] = new
print(sales[name])


#102
list = {}
for i in range(0, 4):
    name = input('입력 : ')
    age = int(input('입력 : '))
    shoes = int(input('입력 : '))
    list[name] = {'age':age, 'shoes size':shoes}
name = input('입력 : ')
print(list[name])


#103
list = {}
for i in range(0, 4):
    name = input('입력 : ')
    age = int(input('입력 : '))
    shoes = int(input('입력 : '))
    list[name] = {'age':age, 'shoes size':shoes}

for name in list:
    print(name, list[name]['age'])

#104
for i in range(0, 4):
    name = input('입력 : ')
    age = int(input('입력 : '))
    shoes = int(input('입력 : '))
    list[name] = {'age':age, 'shoes size':shoes}

getrid = input("입력 : ")
del list[getrid]

for name in list:
    print(name, list[name]['age'], list[name]['shoes size'])

