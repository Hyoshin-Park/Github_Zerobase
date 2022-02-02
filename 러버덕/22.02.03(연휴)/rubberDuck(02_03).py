## CLASS A는 더하기와 빼기의 가능의 함수가 있는 클래스다.
##CLASS B는 곱하기와 나누기의 기능의 함수가 있는 클래스 일 때
## CLASS B 를 사용할 때 CLASS A도 사용할 수 있는 클래스를 만드시오




































class calas:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

class calmd(calas):

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2


mycal = calmd()

print(mycal.add(10,20))
print(mycal.sub(10,20))
print(mycal.mul(10,20))
print(mycal.div(10,20))
