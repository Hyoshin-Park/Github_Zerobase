#80
first_name = input("입력 : ")
print(len(first_name))
last_name = input("입력 : ")
print(len(last_name))
print(len(first_name + " " + last_name))


#81
subject = input("입력 : ")
print(subject + '-')


#82
poetry = input('입력 : ')
start = int(input('시작입력 :'))
end = int(input('끝입력 :'))
# end인덱스출력X
print(poetry[start:end])

#83
upper = input('대문자 입력 : ')
while upper.isupper() == False:
    print('again')
    upper = input('입력 : ')


#84
word = input('입력 : ')  
print(word[0:2].upper())


#85
count = 0
name = input("입력 : ")
for i in range(len(name)):
  if name[i] in ('a','i','o','u','e'):
    count += 1

print(count)



#86
pw1 = input('1 입력 : ')
pw2 = input('2 입력 : ')

if pw1 == pw2:
  print('good')
else:
  #입력한 문자 같은지 확인
  if pw1.upper() == pw2.upper():
    print('대소문자')
  #문자도 안맞는 경우
  else:
    print('안맞음')


#87
word = input('입력 : ')  
for i in range(len(word)-1,-1,-1):
  print(word[i])