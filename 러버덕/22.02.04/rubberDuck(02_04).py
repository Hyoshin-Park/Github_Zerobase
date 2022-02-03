#### 사용자에게 숫자를 받고 각각 짝수 홀수 실수를 구분하여 리스트에 넣어보자
#### 잘못된 입력을 받아도 에러가 뜨지 않게 try except를 사용한다.


#### with as 를 사용하여 "c:/pythonTxt/test.txt" 를 각각 write(w), read(r) 해보자
#### test.txt에는 밑에 주어진 항목이 한줄마다 출력되게 하시오.

languages = ["C", "C#", "java", "python"]

























#1

evenList = []
oddList = []
floatList = []

n = 1
while n < 6:

    try:
        num = float(input("input number"))
    except:
        print("Exception raise")
        print("input number again!!!")
        continue

    else:
        if num - int(num) != 0:
            print("float number")
            floatList.append(num)
        else:
            if num % 2 == 0:
                print("even number")
                evenList.append(num)
            else:
                print("odd number")
                oddList.append(num)

        n += 1


print(f"evenList: {evenList}")
print(f"oddList: {oddList}")
print(f"floatList: {floatList}")


#2

languages = ["C", "C#", "java", "python"]


uri = "c:/pythonTxt/"

for item in languages:
    with open(uri + "test.txt", "w") as f:
        f.write(item)
        f.write("\n")



with open(uri + "test.txt", "w") as f:
    f.writelines(item + "\n" for item in languages)
