#20

name = input("Enter your name: ")

print(len(name))

#21

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

print(fname, lname)

name = fname + " " + lname

print(len(name))

#22

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

name = fname.capitalize() + " " + lname.capitalize()

print(name)

#23

lullaby = input("Enter the first line : ")

print(len(lullaby))

print_lullaby = int(input("Enter the starting Index"))
print_lullaby1 = int(input("Enter the ending Index"))

print(lullaby[print_lullaby:print_lullaby1])

#24

word = input("Enter any word: ")

print(word.upper())

#25

name = input("Enter your first name: ")

if len(name) > 5:
    lname = input("Enter your last name: ")
    full_name = name + lname
    print(full_name.upper())
else:
    print(name.lower())

#26

word = input("Enter a word: ")

first = word[0].lower()
length = len(word)
rest = word[1:length].lower()
if first == "i" or first == "e" or first == "a" or first == "o" or first == "i":
    latin = first + rest + "way"
    print(latin)
else:
    latin1 = rest + first + "ay"
    print(latin1)
