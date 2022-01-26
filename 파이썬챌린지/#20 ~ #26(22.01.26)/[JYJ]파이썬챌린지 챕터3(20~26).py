# 020

name = input("이름이 무엇인가요?: ")
print(len(name))

# 021

firstname = input("이름이 어떻게 되나요?: ")
secondname = input("성이 어떻게 되나요?: ")

name = firstname + " " + secondname

print(name)
print(len(name))

# 022

firstname = input("이름을 소문자로 입력하세요: ")
secondname = input("성을 소문자로 입력하세요: ")

firstname = firstname.title()
secondname = secondname.title()

name = firstname + " " + secondname

print(name)

# 023

line = input('자장가의 첫 줄을 입력: ')
line_length = len(line)
print(line_length)

start_range = int(input("범위 시작 번호: "))
end_range = int(input("범위 끝 번호: "))

print(line[start_range:end_range])

# 024

word = input('아무 단어나 입력하세요:' )
word = word.upper()
print(word)

# 025

name = input("이름을 입력하세요: ")
namelength = len(name)

if namelength < 5:
    secondname = input("성을 입력하세요: ")
    name = name + secondname
    print(name.upper())

else:
    print(name.lower())


# 026 (몰랐던 문제)

word = input("단어를 입력하세요: ")
first = word[0]

# 026

word = input("단어를 입력하세요: ")
first = word[0].lower()
rest = word[1:]

if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    newWord = first + rest + "ay"

else:
    newWord = rest + first + "way"

print(newWord.lower())
