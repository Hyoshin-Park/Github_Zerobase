########[전영주] 문제##########

# 1. 41의 8 제곱근 구하기 (소수점 둘째 자리 까지만 표시)
a = 41 ** (1/8)
print(f"{a:0.2f}")


# 2. 자신의 키를 입력하여 군면제 대상인지 아닌지 확인해보자(140.0cm 이하 = 면제 대상)
height = float(input("키가 몇cm인지 입력하세요. : "))
a = height <= 140
print(f"군면제 대상인가요? : {a}")


# 3. operator 모듈을 이용하여 13과 7의 합, 곱, 나눗셈을 해보자.(나눗셈은 소수점 셋째 자리 까지 표시)
import operator

print(operator.add(13,7))
print(operator.mul(13,7))
print(f"{operator.truediv(13,7):.3f}")



##############[박효신] 문제########

#사용자에게 7 과 3.14 라는 숫자를 이용해 ( + , * , /, // % 혹은 divmod)을
#각각 이용해 더하기 곱하기 나누기 나머지와 몫을 구하는 과정을
# 출력하시오(단, 소수점 두자리까지만 출력이 되게 하세요)

print(f"7 + 3.14는 {(7 + 3.14):.2f}입니다.")
print(f"7 * 3.14는 {(7 * 3.14):.2f}입니다.")
print(f"7 / 3.14는 {(7 / 3.14):.2f}입니다.")
print(f"7 / 3.14를 했을 때의 몫은 {(7 // 3.14):.2f}입니다.")
print(f"7 / 3.14를 했을 때의 나머지는 {(7 % 3.14):.2f}입니다.")




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
#사용자에게 먼저 0에서 1.0 사이에 점수를 입력하라고 알려줍니다

score = float(input("점수를 입력하세요.(0에서 1.0사이) : "))
if score >= 0.9:
    print("A")
elif 0.8 <= score <0.9:
    print("B")
elif 0.7 <= score <0.8:
    print("C")
elif 0.6 <= score <0.7:
    print("D")
elif score < 0.6:
    print("F")
else:
    print("범위에 알맞은 점수를 입력하세요.")