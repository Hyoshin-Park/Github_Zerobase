import random

nums = random.sample(range(0, 50), 20)

print(nums)
inputNum = int(input("input number"))

nearNum = 0
minNum = 50

for n in nums:
    absNum = abs(n - inputNum)

    if absNum < minNum:
        minNum = absNum
        nearNum = n

print(f"{nearNum}")
