class Top5Player:

    def __init__(self, cs, ns):
        self.currentScores = cs
        self.newScore = ns

    def setAlignScore(self):

        nearIdx = 0
        nearScore = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScore )

            if absNum < minNum:
                minNum = absNum
                nearIdx = i
                nearScore = s

        if self.newScore >= self.currentScores[nearIdx]:
            for i in range(len(self.currentScores) - 1, nearIdx - 1):
                self.currentScores[i] = self.currentScores[i - 1]
            self.currentScores[nearIdx] = self.newScore


    def getFinalTopScores(self):
        return self.currentScores



scores = [8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]

top5PlayerScores = [9.12, 8.95, 8.12, 7.90, 7.88]

total = 0
avg = 0
for n in scores:
    total += n

avg = round(total / len(scores), 2)

print(total)
print(avg)

tp = Top5Player(top5PlayerScores, avg)
tp.setAlignScore()
top5PlayerScores = tp.getFinalTopScores()
print(top5PlayerScores)
