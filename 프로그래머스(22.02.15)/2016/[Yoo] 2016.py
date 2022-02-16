def solution(a, b):
    if a == 1:
        c = b
    else:
        c = 0
        for i in range(1, a):
            if i in (1,3,5,7,8,10):
                c += 31
            elif i in (4,6,9,11):
                c += 30
            elif i == 2:
                c += 29
        c += b
    result = c%7
    days = {1:'FRI',2:'SAT',3:'SUN',4:'MON',5:'TUE',6:'WED',0:'THU'}
    return days[result]