def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant

# 코드 실행은 안됐는데 제출 후 채점하기에서 점수를 줌