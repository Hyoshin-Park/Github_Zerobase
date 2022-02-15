def solution(s):
    answer = ''
    s = s.split(' ')  # 공백을 기준으로 문자열 list

    for i in s:  # 한 아이템씩 체크
        for idx, cha in enumerate(i):  # 인덱스와 원소가 둘 다 필요해서 enumerate함수를 사용
            if idx % 2 == 0:
                answer += cha.upper()
            else:
                answer += cha.lower()

        answer += ' '

    return answer[0:-1]  # 출력했는데 마지막에 계속 뛰어쓰기가 들어가서 인덱스 표시함