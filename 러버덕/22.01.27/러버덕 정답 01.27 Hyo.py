# 사용자에게 각각 가로와 세로의 입력을 받아 삼각형과 사각형의 넓이를 구하시오.
#(가로:10, 세로:7를 넣어서 구하시오)(단, 출력은 한줄로 나오게 합니다.)

width = int(input("가로 길이: "))
height = int(input("세로 길이: "))

triangle = width * height / 2
square = width * height

print(f"width: {width}, height: {height}, triangle: {triangle}, square: {square}")
or
print("width: " width, end="")
print("height: " height, end="")
print("triangle: " triangle, end="")
print("square: " square)


#1번을 풀었더니 결과가 3.9 2번을 풀었더니 2.51.4 가 나왔다고 한다
#빈칸을 채워 넣으시오

#1
fNum1 = 2.5
fNum2 = 1.4
print(fNum1 + fNum2)
#2
fNum1 = str(fNum1)
fNum2 = str(fNum2)

print(fNum1 + fNum2)


#보너스 if문 활용

총 급여를 계산하기 위해 입력을 사용하여 사용자에게 시간 및 시간당 비율을 묻는 프로그램을 작성합니다.
최대 40시간의 시간당 비율을 지불하고 40시간 이상 근무한 모든 시간에 대한 시간당 비율의 1.5배를 지불합니다.
45시간과 시간당 8920원의 비율을 사용하여 프로그램을 검정합니다.
입력을 사용하여 문자열을 읽고 float()을 사용하여 문자열을 숫자로 변환해야 합니다.

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40 :
    pay = 40 * r + (h-40)*1.5*r
else :
    pay = h * r
print(pay)
