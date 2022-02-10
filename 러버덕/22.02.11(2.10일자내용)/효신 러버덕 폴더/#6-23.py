# def recusion(num):
#
#     if num > 0:
#         print("*" * num)
#         return recusion(num - 1)
#     else:
#         return 1
#
# recusion(10)
#
# #10!

def factorial(num):

    if num > 0:
        return num * factorial(num-1)
    else:
        return 1

print(factorial(10))
