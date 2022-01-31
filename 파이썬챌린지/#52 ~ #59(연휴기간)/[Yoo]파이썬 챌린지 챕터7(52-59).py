# #52번
# import random
# num = random.randint(1,100)
# print(num)


#53번
# import random
# a = random.choice(['사과', '바나나', '키위', '딸기', '망고'])
# print(a)


# #54번
# import random
# a = random.choice(['앞면', '뒷면'])
# inp = input("앞면과, 뒷면 중 고르세요. : ")

# if a == inp:
#     print("맞혔습니다. ")

# elif a != inp:
#     print("틀렸습니다.")

# print(f"컴퓨터는 {a}를 골랐습니다.")



# #55번
# import random
# a = random.randint(1,5)
# b = int(input("1부터 5까지의 숫자를 선택하세요. : "))

# if a == b :
#     print("맞혔습니다.")
# elif b > a or b < a :
#     if b > a :
#         print("입력하신 숫자가 더 높습니다.")
#         b = int(input("1부터 5까지의 숫자를 선택하세요. : "))
#         if b == a :
#             print("맞혔습니다.")
#         elif b != a :
#             print("틀렸습니다.")
#     else :
#         print("입력하신 숫자가 더 낮습니다.")
#         b = int(input("1부터 5까지의 숫자를 선택하세요. : "))
#         if b == a :
#             print("맞혔습니다.")
#         elif b != a :
#             print("틀렸습니다.")



# #56번
# import random
# a = random.randint(1,10)
# n = int(input("1부터 10까지의 숫자를 입력하세요. : "))
# while a != n:
#     print("틀렸습니다. ")
#     n = int(input("다시 입력하세요. : "))
# print("맞혔습니다.")



# #57번
# import random
# a = random.randint(1,10)
# n = int(input("1부터 10까지의 숫자를 입력하세요. : "))
# while a != n:
#     if n > a :
#         print("입력하신 숫자가 더 큽니다.")
#         n = int(input("다시 입력하세요. : "))
#     elif n < a :
#         print("입력하신 숫자가 더 작습니다.")
#         n = int(input("다시 입력하세요. : "))

# print("맞혔습니다.")



# #58번
# import random
# sum = 0
# for i in range(5):
#     a = random.randint(1,99)
#     b = random.randint(1,99)
#     c = int(input(f"{a}+{b}의 결과를 입력하세요. : "))

#     if (a+b) == c:
#         sum += 1

# print("맞힌 정답의 개수 :", sum)



# #59번
# import random
# my_color = input("RED, BLUE, GREEN, BLACK, YELLOW 중 한가지의 색을 고르세요. : ").upper()
# program_color = random.choice(['RED', 'BLUE', 'GREEN', 'BLACK', 'YELLOW'])

# while my_color != program_color:
#     print(f"You are probably feeling {program_color} right now.")
#     my_color = input("다시 맞혀보세요. : ").upper()
# print("맞혔습니다.")