#69
country_tuple = ('korea','uk','india','hongkong','usa')
print(country_tuple)

country_name = input("입력 : ")
print("index : ", country_tuple.index(country_name))


#70
country_tuple = ('korea','uk','india','hongkong','usa')
country_number = int(input("0~5 입력 : "))
print(country_tuple[country_number])


#71
sports_list = ['tennis','soccer']
sport = input("입력 : ")
sports_list.append(sport)
print(sports_list)



#72
subject_list = ['국어','수학','역사','영어','체육']
subject = input('싫어하는 과목 입력 : ')
subject_list.remove(subject)
print(subject_list)


#73
#key로 지움
food_list = {}
for i in range(1, 5):
    food = input("입력 : ")
    food_list[i] = food
print(food_list)
remove_food = int(input('지우고 싶은 것은? :'))
del food_list[remove_food]
print(food_list)



#74
color_list = ['blue','red','pink','black','green','purple','yellow','white','oragne','magenta']
start_num = int(input("시작번호 : "))
end_num = int(input("끝번호 : "))
print(color_list[start_num:end_num+1])


#75
number_list = [345,567,234,765]
for i in range(len(number_list)):
    print(number_list[i])

number = int(input("입력 : "))
if number in number_list:
    for i in range(len(number_list)):
        if number == number_list[i]:
            print("인덱스 : ", i)
else:
    print("없음")
    
    
    
    
    
#76
name_list = []

for i in range(0,3):
  name = input('입력 : ')
  name_list.append(name)

name = input('더 추가? : y/n : ')
  
while name == 'y':
  name = input('입력 : ')
  name_list.append(name)
  name = input('더 추가? y/n : ')
  
print("초대인원 : ", len(name_list))



#77

name_list = []

for i in range(0,3):
  name = input('입력 : ')
  name_list.append(name)

name = input('더 추가? : y/n : ')
  
while name == 'y':
  name = input('입력 : ')
  name_list.append(name)
  name = input('더 추가? y/n : ')
  
print(name_list)

yn_name = input('이름입력 : ')
yn = input(f"{name_list.index(yn_name)} 삭제?")

if yn == 'y':
  yn_num = name_list.index(yn_name)
  del name_list[yn_num]

print(name_list)




#78
tv_list = ['list1','list2','list3','list4']
for i in range(len(tv_list)):
  print(tv_list[i])

tv_name = input('프로그램 입력 : ')
tv_num = int(input('프로그램 위치 : '))

tv_list.insert(tv_num, tv_name)

print(tv_list)




#79
nums = []
for i in range(0, 3):
  num = int(input('입력 : '))
  nums.append(num)

yn = input("마지막 저장 ? : ")
if yn == 'y':
  print(nums)
else:
  nums.remove(2)
  print(nums)