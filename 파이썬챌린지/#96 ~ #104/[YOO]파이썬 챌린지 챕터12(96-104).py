#96번

a = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

#97번

a = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
i = int(input("행을 입력하세요. : "))
j = int(input("열을 입력하세요. : "))

print(a[i][j])

#98번

a = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
i = int(input("표시할 행을 입력하세요. : "))
print(a[i])
n = int(input("새로운 값을 입력하세요. : "))
a[i].append(n)
print(a[i])


#99번
a = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
i = int(input("표시할 행을 입력하세요. : "))
print(a[i])
j = int(input("열을 선택하세요. : "))
print(a[i][j])
ans = input("이 값을 변경하고 싶으신가요?(y/n) : ").lower()
if ans == 'y':
    new = int(input("새로운 값을 입력하세요. : "))
    a[i][j] = new
print(a[i])



#100번
dict = {"John" : {"N":3056, "S":8463, "E":8441, "W":2694},
"Tom" : {"N":4832, "S":6786, "E":4737, "W":3612},
"Anne" : {"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona" : {"N":3904, "S":3645, "E":8821, "W":2451}}



#101번
dict = {"John" : {"N":3056, "S":8463, "E":8441, "W":2694},
"Tom" : {"N":4832, "S":6786, "E":4737, "W":3612},
"Anne" : {"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona" : {"N":3904, "S":3645, "E":8821, "W":2451}}

name = input("이름을 입력하세요. : ")
nation = input("지역을 입력하세요. : ")

print(dict[name][nation])

new_name = input("변경하려는 데이터의 이름을 입력하세요. : ")
new_nation = input("변경하려는 데이터의 지역을 입력하세요. : ")
data = int(input("변경하려는 데이터의 값을 입력하세요. : "))
dict[new_name][new_nation] = data

print(dict[new_name])


#102번
dict = {}
for i in range(4):
    name = input("이름을 입력하세요. : ")
    age = int(input("나이를 입력하세요. : "))
    shoes = input("신발 사이즈를 입력하세요. : ")
    dict[name] = {'나이' : age , '신발사이즈' : shoes}

n = input("입력된 이름들 중 하나를 입력하세요. : ")
print(dict[n])



#103번
dict = {}
for i in range(4):
    name = input("이름을 입력하세요. : ")
    age = int(input("나이를 입력하세요. : "))
    shoes = input("신발 사이즈를 입력하세요. : ")
    dict[name] = {'나이' : age , '신발사이즈' : shoes}

for i in dict:
    print(f'이름 : {i} / 나이 : {dict[i]["나이"]}')




#104번
dict = {}
for i in range(4):
    name = input("이름을 입력하세요. : ")
    age = int(input("나이를 입력하세요. : "))
    shoes = input("신발 사이즈를 입력하세요. : ")
    dict[name] = {'나이' : age , '신발사이즈' : shoes}

remove_name = input("목록에서 제거하고 싶은 이름을 입력하세요. : ")
del dict[remove_name]
for i in dict:
    print(f"이름 : {i}, 나이 : {dict[i]['나이']}, 신발사이즈 : {dict[i]['신발사이즈']}")