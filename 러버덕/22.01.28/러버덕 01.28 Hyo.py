#사용자에게 7 과 3.14 라는 숫자를 이용해 ( + , * , /, // % 혹은 divmod)을
#각각 이용해 더하기 곱하기 나누기 나머지와 몫을 구하는 과정을
# 출력하시오(단, 소수점 두자리까지만 출력이 되게 하세요)



#0에서 1.0 사이의 점수를 묻는 프로그램을 작성한다.
#점수가 범위를 벗어나면 오류를 출력합니다.
#점수가 0.0~1.0점 사이일 경우 다음 표를 이용하여 Grade를 출력한다.
#점수 등급
#>= 0.9A
#>= 0.8B
#>= 0.7C
#>= 0.6D
#< 0.6F
#사용자가 입력한 값이 범위를 벗어나면 해당 에러메시지를 출력하여 종료합니다.




















num1 = int(input("Enter a number"))
num2 = int(input("Enter a number1"))

plus = num1 + num2
minus = num1 - num2
mult = num1 * num2
divid = divmod(num1, num2)
#divid = num1 // num2
#rest = num1 % num2

print("plus : %.2f" % plus)
print("minus : %.2f" % minus)
print("mult : %.2f" % mult)
print("divid : %.2f" % divid)
print(f"몫은 {divid}, 나머지는 {rest}입니다")









score = input("Enter Score:")
scorefloat = float(score)
if scorefloat > 1 or scorefloat < 0 :
    print("Out of range")
elif scorefloat >= 0.9 :
    print("A")
elif scorefloat >= 0.8 :
    print("B")
elif scorefloat >= 0.7 :
    print("C")
elif scorefloat >= 0.6 :
    print("D")
elif scorefloat < 0.6 :
    print("F")
