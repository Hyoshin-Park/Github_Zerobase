# 0126
# 20 - 26 : 문자열

#20 : 사용자에게 이름을 요청하고 그 이름의 길이를 출력하라
name = input("Enter a name : ")
print("name is " + name)
print("name length is ", len(name))

# 21 : 사용자에게 이름을 묻고 그 다음으로 성을 묻는다. 이름과 성 사이에 공백 하나를 두어 출력하고 공백을 포함한 전체 이름의 길이를 출력하라
first_name = input("Enter a first name : ")
last_name = input("Enter a last name : ")
print("name is " + first_name + " " + last_name)
print("name length is ", len(first_name + " " + last_name))
# 22 : 사용자에게 이름과 성을 소문자로 입력하라고 요청한다. 각 첫 문자만 대문자로 변경하고 이름과 성 사이에 공백을 하나 두어 결합한 후 그 결과를 출력하라
first_name = input("Enter a first name(lowercase) : ")
last_name = input("Enter a last name(lowercase) : ")
first_name = first_name.capitalize()
last_name = last_name.capitalize()
print(first_name + " " + last_name)

# 23 : 사용자에게 자장가의 첫 줄을 입력하라고 요청하고 그 문자열의 길이를 출력한다 사용자에게 범위를 시작할 인덱스 번호를 묻고 범위의 끝 인덱스 번호를 묻는다 그런 후 그 범위의 텍스트를 출력하라 파이썬에서 인덱스는 1이 아닌 0부터 시작한다는 것을 기억하자
lullaby = input("Lullaby : ")
print("Lullaby length : " , len(lullaby))
start_index = input("start index : ")
start_index = int(start_index) - 1
last_index = int(input("last_index : "))
print("Lullaby : " + lullaby[start_index:last_index])

# 24 : 사용자에게 아무 단어나 입력하라고 하고 그것을 대문자로 출력하라
word = input("Enter a word : ")
print(word.upper())

# 25 : 사용자에게 이름을 입력하라고 요청한다 만약 이름의 길이가 5자 미만이면 성을 입력하라고 요청하고 중간 공백 없이 이름과 성을 결합하고 대문자로 출력하라 만약 이름의 길이가 5자 이상이면 이름을 소문자로 출력하라
name = input("Enter a name :" )
if len(name) < 5:
  last_name = input("Enter a last name : ")
  print((name + last_name).upper())
else:
  print(name.lower())

# 26 : 피그 라틴은 단어의 첫 자음을 가져와서 단어 끝으로 이동하고 마지막에 'ay'를 추가한다 만약 단어가 모음으로 시작한다면 단어의 끝에 그냥 'way'를 붙인다 예를 들어 'pig'라는 단어는 'igpay', 'banana'는 'ananabay', 그리고 'aadvark'는 'aadvarway'가 된다 사용자에게 단어를 입력받아서 피그 라틴으로 변환하고 소문자로 출력하는 프로그램을 만들어라
word = input("word : ")
f_word = word[0]
len = len(word)
if word[0] in ('a','e','i','o','u'):
  print(word + 'way')
else:
  word = word[1:len] + word[0]
  print(word + 'ay')









