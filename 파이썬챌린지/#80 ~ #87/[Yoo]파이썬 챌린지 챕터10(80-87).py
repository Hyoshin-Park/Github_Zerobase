##80
# first_name = input("이름을 입력하세요. : ")
# last_name = input("성을 입력하세요. : ")

# print(f"이름의 길이 : {len(first_name)}")
# print(f"성의 길이 : {len(last_name)}")
# fl = first_name + ' ' + last_name
# print(f"이름과 성 : {fl}")
# print(f"전체 이름의 길이 {len(fl)}")




##81번
# a = input("가장 좋아하는 과목 이름 : ")
# for i in a :
#     print(i, end='-')




##82번
# a = "자세히 보아야 예쁘다 오래 보아야 사랑스럽다 너도 그렇다"
# print(a)
# b = int(input("시작 인덱스를 입력하세요. : "))
# c = int(input("마지막 인덱스를 입력하세요. : "))

# print(a[b:c])


##83번
# while True :
#     a = input("대문자로 메시지를 입력하세요. : ")
#     b = a.upper()
#     if a != b :
#         print("대문자로 다시 입력하세요.")
#     elif a == b:
#         print(a)
#         break




##84번
# eng = input("영단어를 입력하세요. : ").lower()
# eng1 = eng[0:2].upper()
# eng2 = eng[2:]
# print(eng1+eng2)




##85번
# name = input("영문이름을 입력하세요. : ").lower()
# sum = 0
# for i in name:
#     if i in ['a','e','i','o','u']:
#         sum += 1
    
# print(sum)




##86번
# pw1 = input("새로운 비밀번호를 입력해주세요. : ")
# pw2 = input("다시 한 번 입력해주세요. : ")

# if pw1 == pw2:
#     print("감사합니다.")
# elif pw1.lower() == pw2.lower():
#     print("대소문자를 확인해주세요.")
# else :
#     print("일치하지 않습니다.")




##87번
# word = list(input("단어를 입력하세요."))
# word.reverse()
# for i in word:
#     print(i)