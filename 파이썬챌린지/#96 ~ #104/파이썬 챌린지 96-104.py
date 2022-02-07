#96

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

print(list)

#97

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

indexInput1 = int(input("Enter the line Index(0 - 3): "))
indexInput2 = int(input("Enter the row Index(0 - 2): "))

print(list[indexInput1][indexInput2])

#98

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

indexInput1 = int(input("Enter the line Index(0 - 3): "))

print(list[indexInput1])

addInput = int(input(f"Enter a number to add in Index; {indexInput1}: "))

list[indexInput1].append(addInput)

print(list[indexInput1])

#99

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

print(list)

indexInput1 = int(input("Enter the line Index(0 - 3): "))

print(list[indexInput1])

indexInput2 = int(input("Enter the row Index(0 - 2): "))

print(list[indexInput1][indexInput2])

askInput = input("Do you want to change the row Index?(y) or (n): ").lower()

if askInput == "y":
    askInput1 = int(input("What do you want to change to?: "))
    list[indexInput1][indexInput2] = askInput1

print(list[indexInput1])

#100

dict = {John{N: 3056, S = 8463, E = 8441, W = 2694},
        Tom{N: 4832, S = 6786, E = 4737, W = 3612},
        Anne{N: 5239, S = 4802, E = 5820, W = 1859},
        Fiona{N: 3904, S = 3645, E = 8821, W = 2451}}


print(dict)

#101

dict = {"John" :{"N": 3056, "S" : 8463, "E" : 8441, "W": 2694},
        "Tom":{"N": 4832, "S" : 6786, "E" : 4737, "W" : 3612},
        "Anne":{"N": 5239, "S" : 4802, "E" : 5820, "W" : 1859},
        "Fiona":{"N": 3904, "S" : 3645, "E" : 8821, "W" : 2451}}

print(dict)


changeValue = input("Which name do you want to change: ").capitalize()
changeZone = input("Which zone do you want to change: ").upper()
changeZoneInto = int(input("What should I change to?(input zone ): "))

dict[changeValue][changeZone] = changeZoneInto


print(dict[changeValue])

#102

dict = {}

for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoeSize = int(input("Enter shoeSize: "))
    dict[name] = {'Age': age, 'Shoe size': shoeSize}

askName = input("Enter name: ")
print(dict[askName])

#103

dict = {}

for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoeSize = int(input("Enter shoeSize: "))
    dict[name] = {'Age': age, 'Shoe size': shoeSize}


for name in dict:
    print(name,':', dict[name]["Age"])


#104

dict = {}

for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoeSize = int(input("Enter shoeSize: "))
    dict[name] = {'Age': age, 'Shoe size': shoeSize}


nameDel = input("What do you want to delete?: ")
del dict[nameDel]

for name in dict:

    print(name, dict[name])
