def getNearNum(an):

    basscores = [95, 85, 75, 65, 55]
    nearNum = 0
    minNum = 100

    for n in basscores:
        absNUm = abs(n - an)
        if absNUm < minNum:
            minNum = absNUm
            nearNum = n

    if nearNum == 95:
        return "A"
    if nearNum == 85:
        return "B"
    if nearNum == 75:
        return "C"
    if nearNum == 65:
        return "D"
    if nearNum <= 5:
        return "F"





scores = []

kor = int(input("kor scores"))
scores.append(kor)

eng = int(input("eng scores"))
scores.append(eng)

mat = int(input("mat scores"))
scores.append(mat)

sci = int(input("sci scores"))
scores.append(sci)

his = int(input("his scores"))
scores.append(his)

totalScore = sum(scores)

print(f"totalscore is {totalScore}")
avgScore = totalScore / len(scores)
print(f"avg is {avgScore}")


grade = getNearNum(avgScore)
print(grade)
