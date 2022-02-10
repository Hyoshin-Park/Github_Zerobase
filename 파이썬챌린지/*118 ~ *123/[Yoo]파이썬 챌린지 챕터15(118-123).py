##118번
# def a():
#     num = int(input("숫자를 입력하세요. : "))
#     return num

# def b(n):
#     for i in range(1,n+1):
#         print(i)

# b(a())


##119번
# import random

# def num():
#     num1 = int(input("낮은 숫자를 입력하세요. : "))
#     num2 = int(input("높은 숫자를 입력하세요. : "))

#     comp_num = random.randrange(num1,num2)
#     print("I am thinking of a number...")
#     return comp_num

# def th():
#     th_num = int(input("생각하고 있는 숫자를 입력하세요. : "))
#     return th_num

# def cor(n1,n2):
#     while True:
#         if n1 == n2:
#             print("Correct, you win")
#             break
#         elif n1 > n2:
#             print("Low")
#             n2 = int(input("생각하고 있는 숫자를 입력하세요. : "))
#             continue
#         elif n2 < n1:
#             print("High")
#             n2 = int(input("생각하고 있는 숫자를 입력하세요. : "))
#             continue

# cor(num(),th())


##120번
# import random
# def a():
#     a_nums = random.sample(range(5,20), 2)
#     ans = int(input((f"{a_nums[0]} + {a_nums[1]} = ")))
#     a_ans = a_nums[0]+a_nums[1]
#     print(f"your answer : {ans}, answer : {a_ans}")
#     return ans, a_ans

# def b():
#     b_num1 = random.randrange(25, 50)
#     b_num2 = random.randrange(1, 25)
#     ans = int(input((f"{b_num1} - {b_num2} = ")))
#     b_ans = b_num1-b_num2
#     print(f"your answer : {ans}, answer : {b_ans}")
#     return ans, b_ans

# def c(n1,n2):
#     if n1 == n2:
#         print("정답")
#     elif n1 != n2:
#         print("틀림")

# print("1) Addition\n2) Subtraction")
# num = int(input("Enter 1 or 2 : "))
# if num == 1:
#     n1, n2 = a()
#     c(n1, n2)
# elif num == 2:
#     n1, n2 = b()
#     c(n1, n2)
# else:
#     print("1 or 2 !!!!!!!!!!!!!!!!!!!!")



##121번
#이름 목록을 쉽게 관리할 수 있는 프로그램 생성
#이름 추가 메뉴, 이름 수정 메뉴, 이름 삭제 메뉴, 모든 이름 표시 메뉴를 화면에 표시
#또한 프로그램 종료 메뉴
#다른 걸 선택하면 적절한 메시지
#메뉴 작업이 끝나면 다시 메뉴가 표시 되도록한다.

# names = []

# def add():
#     name = input("추가하고 싶은 이름을 입력하세요. : ")
#     names.append(name)
#     return names

# def rev():
#     print(names)
#     name = input("수정하고 싶은 이름을 입력하세요. : ")
#     c_name = input("어떻게 수정하시겠습니까? : ")
#     a = names.index(name)
#     names[a] = c_name
#     return names

# def rem():
#     print(names)
#     name = input("제거하고 싶은 이름을 입력하세요. : ")
#     names.remove(name)
#     return names

# def pri():
#     print(names)


# while True:
#     print("1) 이름 추가\n2) 이름 수정\n3) 이름 삭제\n4) 모든 이름 표시\n5) 프로그램 종류", end="\n")

#     n = int(input(("원하는 메뉴를 골라주세요. : ")))
#     if n == 1:
#         print()
#         add()
#     elif n == 2:
#         print()
#         rev()
#     elif n == 3:
#         print()
#         rem()
#     elif n == 4:
#         print()
#         pri()
#     elif n == 5:
#         break
#     else:
#         print()
#         print("메뉴에 있는 숫자를 눌러주세요.")





##122번
# import csv

# def csv():
#     file = open("C:/Users/Yoo/Desktop/MINU/Coding/Salaries.csv",'a')
#     a = input("이름을 입력하세요. : ")
#     b = input("시급을 입력하세요. : ")
#     c = a + ',' + b + '\n'
#     file.write(c)
#     file.close()


# def view():
#     file = open("C:/Users/Yoo/Desktop/MINU/Coding/Salaries.csv",'r')
#     for i in file:
#         print(i)




# while True:
#     selection = int(input("1) Add to file\n2) View all records\n3) Quit program\n\n Enter the number of your selection: "))

#     if selection == 1:
#         csv()
#     elif selection == 2:
#         view()
#     elif selection == 3:
#         break
#     else :
#         print("Only 1,2,3 !!")




##123번
# import csv
# li = []
# def csv():
#     file = open("C:/Users/Yoo/Desktop/MINU/Coding/Salaries.csv",'a')
#     a = input("이름을 입력하세요. : ")
#     b = input("시급을 입력하세요. : ")
#     c = a + ',' + b + '\n'
#     li.append(c)
#     file.write(c)
#     file.close()


# def view():
#     file = open("C:/Users/Yoo/Desktop/MINU/Coding/Salaries.csv",'r')
#     for i in file:
#         print(i)

# def delete():
#     li = []
#     file = open("C:/Users/Yoo/Desktop/MINU/Coding/Salaries.csv",'r')
#     for i in file:
#         li.append(i)
    
#     for idx, i in enumerate(li):
#         print(f"{idx} : {i}")
    
#     d = int(input("삭제하고 싶은 항목의 번호를 입력하세요. : "))
#     del li[d]
#     file.close()

#     file = open("C:/Users/Yoo/Desktop/MINU/Coding/Salaries.csv",'w')
#     for i in li:
#         file.write(i)
    
#     file.close()





# while True:
#     selection = int(input("1) Add to file\n2) View all records\n3) Delete a record\n4) Quit program\n\n Enter the number of your selection: "))

#     if selection == 1:
#         csv()
#     elif selection == 2:
#         view()
#     elif selection == 3:
#         delete()
#     elif selection == 4:
#         break
#     else :
#         print("Only 1,2,3 !!")