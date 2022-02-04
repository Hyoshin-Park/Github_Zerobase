#[전영주]
# 01
"""
n1 = 10; n2 = 0
print(n1 / n2)
print(n1 * n2)
print(n1 - n2)
print(n1 + n2)
위에 식에서 print(n1 / n2) 때문에 문제가 발생한다. try ~ except를 이용하여 문제가 발생했을시 오류를 '예상치 못한 예외가 발생했습니다.'라고 출력하고 남은 식을 출력해라
"""
# n1 = 10; n2 = 0
# try:
#     print(n1/n2)
# except:
#     print("예상치 못한 예외가 발생했습니다.")
# print(n1 * n2)
# print(n1 - n2)
# print(n1 + n2)




#[박효신]
#1
#### 사용자에게 숫자를 받고 각각 짝수 홀수 실수를 구분하여 리스트에 넣어보자
#### 잘못된 입력을 받아도 에러가 뜨지 않게 try except를 사용한다.
# even_list = []
# odd_list = []
# float_list = []
# n = 1
# while n<11:
#     try :
#         num = float(input("숫자를 입력하세요."))
#     except:
#         print("올바른 숫자를 입력하세요.")
#         continue
#     if num - int(num) == 0:
#         if num % 2 == 0:
#             even_list.append(int(num))
#             n+=1
#         elif num % 2 != 0 :
#             odd_list.append(int(num))
#             n+=1
#     elif num != int(num):
#         float_list.append(num)
#         n+=1
# print(f"짝수 : {even_list}")
# print(f"홀수 : {odd_list}")
# print(f"실수 : {float_list}")



# #2
# #### with as 를 사용하여 "c:/pythonTxt/test.txt" 를 각각 write(w), read(r) 해보자
# with open("c:/pythonTxt/test.txt", 'w') as f:
#     f.write("write")

# with open("c:/pythonTxt/test.txt", 'r') as file:
#     file.read('r')



#3
#### test.txt에는 밑에 주어진 항목이 한줄마다 출력되게 하시오.

# languages = ["C", "C#", "java", "python"]
# for i in languages:
#     with open("c:/pythonTxt/test.txt", 'a') as f:
#         f.write(i)
#         f.write('\n')