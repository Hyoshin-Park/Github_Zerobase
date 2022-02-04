# while

#45
total = 0

while total <= 50:
    num = int(input("입력 : "))
    total += num
    print("the total is : ", total)

#46
num = 0
while num <= 5:
    num = int(input("입력 : "))
print("마지막 숫자는 : ", num)


#47 ★

num_1 = int(input("입력 1: "))
num_2 = int(input("입력 2: "))
yn = input("더하기? y/n :")

while yn == 'y':
    num_1 = num_1 + num_2
    num_2 = int(input("입력 : "))
    yn = input("더하기? y/n :")

print("총합 : ", num_1 + num_2)



#48
yn = 'y'
count = 0

while yn == 'y':
    name = input("입력 : ")
    count += 1
    print(name, "은 이미 초대함")
    yn = input("더 초대? y/n :")

print("초대한 인원은 : ", count, "명")


#49
# 질문 변수 a,b 를 입력 받았을 때 어느 쪽이 더 큰지 알 수 있는 방법ㅇㅣ 있나?
# 코드로 a > b, b > a 이런식으로 true false 말고 더 방법이 없나?
# 맞춘 것도 숫자에 포함하나?

compnum = 50
count = 1
num = int(input("입력 : "))

while num != compnum:
    count += 1
    if num > compnum:
        print("더 작게")
    else:
        print("더 크게")
    num = int(input("입력 : "))

print("정답! ", count,"번 걸림")


#50
num = int(input("10~20 중 입력 : "))
while (num <= 10) or (num >= 20):
    if num <= 10:
        print("더 크게")
    elif num >= 20:
        print("더 작게")

    num = int(input("10~20 중 다시 입력 : "))
print("고맙습니다")

#51 ★
num = 10
while num != 0:
    print("♭", num, "개 초록 병이 있는데 ~")
    print("♭ 병이 하나 깨졌네")
    print("♭ 몇 개 병이 남았지")
    num -= 1
    bottle = int(input("숫자 입력 : "))
    
    if num != bottle:
        if num == 0:
            print("병 없음")
        print("다시")
    else:
        print(num, "개 병이 남았네")
        num = 0

