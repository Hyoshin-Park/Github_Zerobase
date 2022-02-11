# 병합정렬
# 자료구조를 분할하고 각각의 분할된 자료구조를 정렬한 후 다시 병합하여 정렬한다
"""
ex)앞에서 배운 정렬보다 속도면서 향상된 정렬

         8,1,4,3,2,5,10,6            #반으로 쪼갬

    8,1,4,3          2,5,10,6        ↓ 분할 단계

 8,1      4,3       2,5     10,6

 8 , 1  , 4,  3,    2 ,  5,     10, 6

#자료구조를 분할하고 각각의 자료구조를 크기 별로 정렬한 후 다시 합침

8 , 1  , 4,  3,    2 ,  5,     10, 6

  1, 8 ,  3, 4  ,    2, 5,     6,10    ↓ 병합 단계

    1,3,4,8      ,     2,5,6,10

          1,2,3,4,5,6,8,10
"""
# 병합정렬 알고리즘을 사용하기 위해 재귀 함수를 사용

def mSort(ns):

    if len(ns) < 2:             # 2보다 작으면 1개니까 더 이상 쪼갤 수가 없어서 리턴을 해줌
        return ns

    midIdx = len(ns) // 2        # 반(half)에 해당되는 midIdx를 구함
    leftNums = mSort(ns[0:midIdx])               # 왼쪽과 오른쪽을 가름
    rightNums = mSort(ns[midIdx:len(ns)])        # 1개가 남을 때 까지 계속 쪼갬 1개가 남으면 다시 병합

    mergeNums = []                             # 이제 다시 병합
    leftIdx = 0
    rightIdx = 0

    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if leftNums[leftIdx] < rightNums[rightIdx]:                           #자리 바꿈 하는 코드
            mergeNums.append(leftNums[leftIdx])
            leftIdx += 1

        else:
            mergeNums.append(rightNums[rightIdx])
            rightIdx += 1
    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]

    return mergeNums

nums = [8, 1, 4, 3, 2, 5, 10, 6]
print(f'mSort(nums) : {mSort(nums)}')

#######################################################################################
# 퀵정렬
# 기준 값(중앙값)보다 작은 값과 큰 값으로 분리한 후 다시 합친다.
"""
ex)
                    8,1,4,3,2,5,4,10,6,8       # 5를 기준으로

        1,4,3,2,4            5          8,10,6,8

  1,2    3     4,4             5              6     8,8,10

  1,2    3     4,4           5                6     8,8,10

"""

def qSort(ns):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2       # 전체 길이를 2로 나는 몫을 기준 인덱스(미드인덱스)로 정의
    midVal = ns[midIdx]         # 그 가운데 있는 값을 midVal기준값         #기준값을 기준으로 왼쪽에 있는녀석들과 오른쪽에 있는 녀석들로나눔

    smallNums = []              # 기준값에서 왼쪽에 있는 아이템을 smallnumms
    sameNums = []               # 기준값과 같은 아이템을 sameNums
    bigNums = []                # 오른쪽에 있는 아이템을 bigNums

    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n == midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)

    return qSort(smallNums) + sameNums + qSort(bigNums)       # 왼쪽에있는 스몰넘즈 + 같은거 + 오른쪽에 있는 빅넘즈를 호출한 곳으로 보내줌

nums = [8,1,4,3,2,5,4,10,6,8]
print(f'qSort(nums) : {qSort(nums)}')