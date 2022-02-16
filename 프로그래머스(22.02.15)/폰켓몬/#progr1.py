def solution(nums):
    num = 0
    answer = list(set(nums))
    count = len(nums) // 2
    for value in answer:
        if (num < count):
            num += 1

    return num
