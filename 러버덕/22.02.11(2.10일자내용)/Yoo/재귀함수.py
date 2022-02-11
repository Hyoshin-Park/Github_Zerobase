##재귀함수

# def recusior(num):
#     if num > 0:
#         print('*'*num)
#         return recusior(num-1)
#     else:
#         return 1

# recusior(10)

def factorial(num):

    if num > 0:
        return num * factorial(num-1)
    else:
        return 1

print(factorial(5))



###########실습#############
##유클리드 호제법
##두 자연수 n1,n2에 대하여 (n1>n2)n1를 n2로 나눈 나머지를 r이라고 할 때,
##n1과 n2의 최대공약수는 n2와 r의 최대공약수와 같다.
# def gcd(n1, n2):
#     if n1 % n2 == 0:
#         return n2
#     else:
#         return gcd(n2, (n1%n2))
# print(gcd(13,5))