# 01
"""
n1 = 10; n2 = 0

print(n1 / n2)
print(n1 * n2)
print(n1 - n2)
print(n1 + n2)

위에 식에서 print(n1 / n2) 때문에 문제가 발생한다. try ~ except를 이용하여 문제가 발생했을시 오류를 '예상치 못한 예외가 발생했습니다.'라고 출력하고 남은 식을 출력해라
"""











# 01 풀이

n1 = 15; n2 = 0

try:
    print(n1 / n2)
except:
    print('예상치 못한 예외가 발생했습니다.')

print(n1 * n2)
print(n1 - n2)
print(n1 + n2)

