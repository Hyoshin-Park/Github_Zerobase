#012 두 개의 숫자를 입력받는다. 만약 첫 번째 숫자가 두 번째 숫자보다 크면, 두 번째 숫자를 먼저 출력한 다음에 첫 번째 숫자를 출력하라.
#그렇지 않다면 첫 번째 숫자를 출력한 다음에 두 번째 숫자를 출력하라

num1 = int(input('첫 번째 숫자: '))
num2 = int(input('두 번째 숫자: '))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

#013 사용자에게 20보다 작은 숫자를 입력하라고 요청한다. 만약 입력된 값이 20과 같거나 크면 "Too high" 라는 메세지를 출력하라. 그렇지 않다면 "Thank you"를 출력하라

number = int(input("20보다 작은 숫자: "))

if number >= 20:
    print("\"Too high\"")

else:
    print("\"Thank you\"")

#014 사용자에게 10과 20(포함) 사이의 숫자를 입력하라고 요청한다. 만약 입력한 값이 이 범위 안의 숫자이면 "Thank you"라는 메시지를 출력하라.
#그렇지 않다면 "Incorrect answer"라는 메세지를 출력하라.

number = int(input('10이상 20이하의 숫자: '))

if number >= 10 and number <= 20:
    print("Thank you")
else:
    print("Incorrect answer")

#015 사용자에게 좋아하는 색을 입력하라고 요청한다. 만약 "red"나 "RED" 또는 "Red"를 입력하면 "I like red too"라는 메세지를 출력하라
#그렇지 않다면 "I don't like that colour, I prefer red"라는 메세지를 출력하라.

favorite = input("좋아하는 색: ")

if favorite == 'red' or favorite == 'RED' or favorite == 'Red':
    print("I like red too")

else:
    print("I don't like that colour, I prefer red")

#016 사용자에게 지금 비가 오는지 묻고 그 대답을 소문자로 변환하여 대소문자에 상관없도록 한다. 만약 "yes"라고 입력한다면 바람이 부는지 묻는다.
#두 번째 질문에 대해 "yes"라고 입력하면 "It is too windy for an umbrella"라는 메시지를 표시하라. 그렇지 않다면 "Take an umbrella"라는 메세지를
#표시하라. 만약 첫 번째 질문에 대해 "yes"라고 입력하지 않는다면 "Enjoy your day"라는 메시지를 표시하라.

rain = input("지금 비가 오나요?: ")

if rain == "yes":
    wind = input("바람이 부나요?: ")
    if wind == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")

else:
    print("Enjoy your day")

#017 사용자의 나이를 묻자. 만약 18세 이상이면 "You can vote"라는 메시지를 표시하라. 만약 17세라면 "You can learn to drive"라는
#메시지를 표시하라. 만약 16세 라면 "You can buy a lottery ticket"이라는 메시지를 표시하라. 만약 16세 미만이라면 "You can go
#Trick-or-treating"이라는 메시지를 표현하라

age = int(input("몇 살인가요?: "))

if age >= 18:
    print("You can vote")

elif age == 17:
    print("You can learn to drive")

elif age == 16:
    print("You can buy a lottery ticket")

else:
    print("You can go Trick-or-treating")

#018 사용자에게 숫자를 입력하라고 요청하자. 만약 10 미만이면 "Too low"라는 메시지를 표시하라. 만약 입력한 숫자가 10에서 20 사이라면
#"Correct"라고 표시하라. 그렇지 않다면 "Too high"라고 표시하라.

number = int(input("숫자를 입력하세요: "))

if number < 10:
    print("Too low")

elif 10 < number < 20:
    print("Correct")

else:
    print("Too high")

#019 사용자에게 1이나 2또는 3을 입력하라고 하자. 만약 1을 입력하면 "Thank you"라는 메시지를 표시하라. 만약 2를 입력하면 "Well done"을
#표시하라. 만약 3을 입력하면 "Correct"를 표시하라. 만약 사용자가 다른 것을 입력하면 "Error message"를 표시하라.

number = int(input("1이나 2또는 3을 입력하시오: "))

if number == 1:
    print("Thank you")

elif number == 2:
    print("Well done")

elif number == 3:
    print("Correct")

else:
    print("Error message")