def solution(n1,n2):
    n1.sort();n2.sort()
    for i in range(len(n2)):
        if n1[i] != n2[i]:
            return n1[i]
        
    return n1[-1]