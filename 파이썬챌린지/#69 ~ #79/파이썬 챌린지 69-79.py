#69

country = ["Korea", "Italy", "France", "Canada", "Spain"]
print(country)

inputCountry = input("Enter a country: ")

print(country.index(inputCountry))

#70

country_tuple = ["Korea", "Italy", "France", "Canada", "Spain"]
print(country_tuple)

inputCountry = int(input("Enter the country index(starting from '0'): "))

print(country_tuple[inputCountry])

#71

sports_list = ["Soccer", "Baseball"]
sports_list1 = ["Tennis", "Table Tennis"]

print(sports_list)
print(sports_list1)

inputFavSports = input("What is your favorite sports?: ")
sports_list.append(inputFavSports)
sports_list1.append(inputFavSports)

print(sorted(sports_list1))
print(sorted(sports_list))

#72

subject = ["Math", "English", "Science", "Art", "Physics", "History"]

print(subject)

subject.remove(input("which subject do you dislike?: "))

print(subject)


#73

food_dict = {}

for i  in range(1,5):
    foodInput = input("What food do you like?(name four): ")
    food_dict[i] = foodInput

print(food_dict)

chooseFood = int(input("Which one is the most less likely to eat?(choose with number): "))

del food_dict[chooseFood]

print(food_dict)

#74

color = ["blue", "green", "purple", "grey", "brown", "pink", "orange", "red", "beige", "yellow"]

firstNum = int(input("Choose a starting number between 0 and 4: "))
secNum = int(input("Choose a end number between 5 and 9: "))
print(color[firstNum:secNum])

#75

num_list = [123, 456, 789, 147]

for i in num_list:
    print(i)

num1 = int(input("Enter a 3-dight number: "))

if num1 in num_list:
    print(num_list.index(num1))

else:
    print("That is not in the list")


#76

name_list = []

for i in range(0, 3):
    name_list.append(input("Enter three friends to invite: "))


flag = True

while flag == True:
    moreName = input("Enter a new friend 'y' or 'n': ")
    if moreName == "y":
        name_list.append(input("Enter a new friend to invite: "))
    elif moreName == "n":
        print(f"There are {len(name_list)} friends in the party")
        flag = False


#77

name_list = []

for i in range(0, 3):
    name_list.append(input("Enter three friends to invite: "))


flag = True

while flag == True:
    moreName = input("Enter a new friend 'y' or 'n': ")
    if moreName == "y":
        name_list.append(input("Enter a new friend to invite: "))
    elif moreName == "n":
        print(name_list)
        flag = False


friend = input("Choose one friend: ")
print(f"His index is {name_list.index(friend)}")

realInvite = input("Do you really want to invite him? 'y' or 'n': ")

if realInvite == "y":
    print("Its good to go")
elif realInvite == "n":
    name_list.remove(friend)

print(name_list)

#78

tvShow = ["1박2일", "무한도전", "런닝맨", "라디오스타"]

for i in tvShow:
    print(i)

insertTvshow = input("Enter a program you want to add: ")
posiTvshow = int(input("Enter which position you want to add(starting from 0): "))

tvShow.insert(posiTvshow, insertTvshow)

for i in tvShow:
    print(i)


#79

nums = []

for i in range(0, 3):
    addNums = int(input("Enter number to add in list: "))
    nums.append(addNums)

print(nums)

if len(nums) == 3:
    saveLast = input("insert last number (y) or (n): ")
    if saveLast == "y":
        print("Good to go")
    elif saveLast == "n":
        del nums[2]

print(nums)
