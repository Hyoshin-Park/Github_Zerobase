#69번
contry = ('한국', '중국', '일본', '미국', '영국')
print(contry)
a = input("다섯개의 국가 이름들 중 하나를 입력하세요 : ")
print(contry.index(a))


#70번
contry = ('한국', '중국', '일본', '미국', '영국')
print(contry)
num = int(input("숫자를 입력하세요 : "))
print(contry[num])



#71번
sports = ['soccer', 'football']
sport = input("좋아하는 운동이 무엇인지 영문으로 작성하세요. : ")
sports.append(sport)
sports.sort()
print(sports)



#72번
a = ['국어', '영어', '수학', '물리', '화학', '생물']
print(a)
hate = input("위 6개의 과목 중 싫어하는 과목을 골라주세요. : ")
a.remove(hate)
print(a)



#73번
d = {}
n_d = {}
for i in range(1,5):
    d[i] = input("좋아하는 음식을 입력하세요. : ")
print(d)

a = int(input("제거하고 싶은 항목을 입력하세요. : "))
del d[a]

l = list(d.values())

for i in range(1, len(l)+1):
    n_d[i] = l[i-1]
print(n_d)



#74번
a = ['빨간색','주황색','노란색','초록색','파란색','남색','보라색','검은색','분홍색','흰색']
num1 = int(input("0에서 4까지의 번호를 입력하세요. : "))
num2 = int(input("5에서 9까지의 번호를 입력하세요. : "))

print(a[num1:num2])



#75번
num_list = [111,222,333,444]
for i in num_list:
    print(i)

num = int(input("세 자리 숫자를 입력하세요 : "))

if num in num_list:
    print(num_list.index(num))
elif num not in num_list:
    print("That is not in the list")



#76번
party = []
for i in range(3):
    party.append(input("파티에 초대할 사람의 이름을 입력하세요. : "))
while True:
    more = input("추가할 사람이 있나요?(y/n) : ")
    if more == 'y':
        party.append(input("파티에 초대할 사람의 이름을 입력하세요. : "))
    elif more == 'n':
        print(f"파티에 초대된 사람은 {len(party)}명입니다.")
        break




#77번
party = []
for i in range(3):
    party.append(input("파티에 초대할 사람의 이름을 입력하세요. : "))
while True:
    more = input("추가할 사람이 있나요?(y/n) : ")
    if more == 'y':
        party.append(input("파티에 초대할 사람의 이름을 입력하세요. : "))
    elif more == 'n':
        print(f"파티 초대 리스트 {party}")
        break
p = input("리스트에 있는 사람들 중 한 명을 입력하세요. : ")
print(party.index(p))
a = input(f"{p}님을 정말로 초대하시겠습니까?(y/n) : ")
if a == 'y':
    print(party)
elif a == 'n':
    party.remove(p)
    print(f"파티 초대 리스트 {party}")




#78번
tv = ['런닝맨', '1박 2일', '무한도전', '스우파']
for i in tv:
    print(i)
a = input("다른 프로그램을 입력하세요. : ")
b = int(input("몇 번째 인덱스에 추가하고 싶으신가요? : "))
tv.insert(b, a)
for i in tv:
    print(i)



#79번
nums = []
for i in range(3):
    num = int(input("숫자를 입력하세요. : "))
    nums.append(num)
a = input("마지막 숫자를 저장하시겠습니까?(y/n) : ")
if a == 'n':
    del nums[(len(nums)-1)]
print(nums)