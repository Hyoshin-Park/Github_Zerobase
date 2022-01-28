# # 35번

# name = input("이름을 입력하세요 : ")
# for i in range(3):
#     print(name)



# # 36번

# name = input("이름을 입력하세요 : ")
# num = int(input("반복할 숫자를 입력하세요. : "))

# for i in range(num):
#     print(name)


# # 37번

# name = input("이름을 입력하세요. : ")

# for i in name:
#     print(i)


# # 38번

# name = input("이름을 입력하세요 : ")
# num = int(input("반복할 숫자를 입력하세요. : "))

# for i in range(num):
#     for i in name:
#         print(i)


# # 39번

# num = int(input("1부터 12까지의 숫자를 입력하세요. : "))

# for i in range(1, 13):
#     print(i*num)


# # 40번

# num = int(input("50미만의 숫자를 입력하세요. : "))

# for i in range(50,num-1, -1):
#     print(i)



# # 41번

# name = input("이름을 입력하세요 : ")
# num = int(input("숫자를 입력하세요. : "))

# if num < 10:
#     for i in range(num):
#         print(name)
# elif num >= 10 :
#     for i in range(3):
#         print("Too high")



# # 42번

# total = 0
# for i in range(5):
#     num = int(input("숫자를 입력하세요. : "))
#     ans = input("입력한 숫자를 total에 더하겠습니까?(Y/N) : ")
#     if ans == "Y":
#         total += num

# print(total)


# # 43번
# direction = input("원하는 카운트 방향을 입력하세요.(Up/Down) : ")
# direction = direction.lower()

# if direction == 'up':
#     num = int(input("가장 큰 수를 입력하세요. : "))
#     for i in range(1, num+1):
#         print(i)
# elif direction == 'down' :
#     num = int(input("20미만의 숫자를 입력하세요. : "))
#     for i in range(20, num-1, -1):
#         print(i)
# else:
#     print("I don't understand")


# #44번
# p = int(input("파티에 몇 명을 초대하고 싶으신가요? : "))

# if p < 10 :
#     for i in range(p):
#         name = input("이름은 무엇인가요? : ")
#         print(f"{name}님이 초대되었습니다. ")
# elif p >= 10 :
#     print("Too many people")