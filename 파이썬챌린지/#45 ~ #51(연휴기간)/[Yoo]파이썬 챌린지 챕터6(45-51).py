# #45

# total = 0

# while total <= 50:
#     a = int(input("숫자를 입력하세요. : "))
#     total += a
#     print(f"숫자의 합은 {total}입니다.")



# #46
# a = 0
# while a <= 5 :
#     a = int(input("숫자를 입력하세요. : "))
# print(f"마지막에 입력하신 숫자는 {a}입니다.")



# # 47번

# a = int(input("숫자를 입력하세요 : "))
# b = int(input("숫자를 입력하세요 : "))

# sum = a + b

# while True:
#     ans = input("또 다른 숫자를 더하고 싶으신가요? ").lower()
#     if ans == 'y':
#         c = int(input("숫자를 입력하세요 : "))
#         sum += c
#     else:
#         break

# print(sum)



# #48번

# cnt = 0
# another = 'y'
# while another == 'y':
#     party = input("초대하고 싶은 사람의 이름을 입력하세요. : ")
#     print(f"{party}님은 초대되었습니다.")
#     cnt += 1
#     another = input("다른 사람을 더 초대하고 싶은가요?(Y/N) : ").lower()
# print(cnt)



# #49번

# compnum = 50

# cnt = 1
# a = int(input("숫자를 입력하세요. : "))
# while a != 50:
#     if a > 50:
#         cnt += 1
#         print("입력하신 숫자가 더 높습니다.")
#         a = int(input("다시 맞춰보세요. : "))
#     elif a < 50:
#         cnt += 1
#         print("입력하신 숫자가 더 낮습니다.")
#         a = int(input("다시 맞춰보세요. : "))

# print(f"{cnt}번만에 맞췄습니다.")



# #50번
# num = int(input("10과 20사이의 숫자를 입력하세요. : "))

# while num<=10 or num>=20:
#     if num <= 10 :
#         print("Too low")
#         num = int(input("다시 입력하세요. : "))
#     elif num >= 20:
#         print("Too high")
#         num = int(input("다시 입력하세요. : "))

# print("Thank you")




# #51번
# n = 10
# while n > 0:
#     print(f"There are {n} green bottles hanging on the wall, {n} green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
#     a = int(input("how many green bottles will be hanging on the wall?"))
#     while a != n:
#         print("No, try again")
#         a = int(input("how many green bottles will be hanging on the wall?"))
    
#     print(f"There will be {n} green bottles hanging on the wall")
#     n -= 1
# print("There are no more green bottles hanging on the wall")
