def solution(nums):
    answer = []
    for i in nums:
        if i not in answer:
            answer.append(i)
    
    if len(answer) >= len(nums)//2:
        return len(nums)//2
    elif len(answer) < len(nums)//2:
        return len(answer)