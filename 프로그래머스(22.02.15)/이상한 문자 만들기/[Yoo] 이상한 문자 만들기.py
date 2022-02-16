def solution(s):
    cnt = 0
    c = ''
    for i in s:
        if i.isalpha():
            if cnt % 2 == 0 :
                cnt += 1
                c += i.upper()
            else:
                cnt += 1
                c += i.lower()
        else:
            cnt = 0
            c += i
    return c