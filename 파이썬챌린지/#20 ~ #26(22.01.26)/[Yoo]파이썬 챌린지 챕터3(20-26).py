#20
name = input("이름을 적어주세요. : ")
print(len(name))

#21
first_name = input("이름이 무엇인가요? : ")
last_name = input("성이 무엇인가요? : ")
name = first_name +" " + last_name
print(name)
print(len(name))

#22
first_name = input("이름이 무엇인가요?(영문 소문자로 작성) : ")
last_name = input("성이 무엇인가요?(영문 소문자로 작성) : ")
first_name = first_name.capitalize()
last_name = last_name.capitalize()

name = first_name +" " + last_name
print(name)


#23
song = input("자장가의 첫 줄을 입력하세요. : ")
print(f"공백을 포함한 글자의 수는 {len(song)}글자입니다.")

num1 = int(input("몇 번째 글자부터 출력하겠습니까? : "))
num2 = int(input("몇 번째 글자까지 출력하겠습니까? : "))

num1 = num1 - 1

print(song[num1:num2])


#24
eng = input("아무 영단어를 입력하세요. : ")
print(eng.upper())

#25
first_name = input("영문이름을 작성하세요. : ")
len = len(first_name)

if len < 5:
    last_name = input("영문성을 입력하세요. : ")
    name = first_name + last_name
    name = name.upper()
    print(name)

elif len >= 5 :
    print(first_name.lower())

#26
word = input("영단어를 입력하세요. : ")
word = word.lower()

if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    print(word + "way")
else:
    print(word[1:] + word[0] + "ay")