##큰 원판이 작은 원판 위로 갈 수 없다.

##         원판개수, 출발기둥, 도착기둥, 경유기둥
def moveDisc(discCnt, fromBar, toBar, viaBar):
    if discCnt == 1:
        print(f"{discCnt}disc를 {fromBar}에서 {toBar}(으)로 이동!")

    else:
        #(discCnt-1)개들을 경유 기둥으로 이동
        moveDisc(discCnt-1, fromBar, viaBar, toBar)

        #discCnt를 목적 기둥으로 이동
        print(f"{discCnt}disc를 {fromBar}에서 {toBar}(으)로 이동!")

        #(discCnt-1)개들을 도착 기둥으로 이동
        moveDisc(discCnt-1, viaBar, toBar, fromBar)

moveDisc(3,1,3,2)