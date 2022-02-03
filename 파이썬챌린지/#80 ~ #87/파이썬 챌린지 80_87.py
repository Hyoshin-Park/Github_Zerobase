#80

Fname = input("Enter your first name: ")
print(len(Fname))

Lname = input("Enter your last name: ")
print(len(Lname))

fullname = Fname + " " + Lname
print(len(fullname))

#81

sub = input("Enter your favorite subject: ")
for letter in sub:
    print(letter, end="-")

#82

poem = input("Enter a line of a poem: ")
Findex = int(input("Enter the beginning index: "))
Lindex = int(input("Enter the last index: "))

print(poem[Findex:Lindex])

#83

msg = input("Enter a message in upper case!!!: ")

flag = True

while flag:
    if msg.isupper():
        print("It is good to go")
        flag = False
    else:
        print("Enter in uppercase plz!!!!!")
        msg = input("Enter a message in upper case!!!: ")

#84

word = input("Enter a word: ")

word1 = word[0:2]
word2 = word[2:]


print(word1.upper(), end="")
print(word2.lower())

#85

name = input("Enter your name: ")

n = 0
name = name.lower()
for letter in name:
    if letter == "a" or letter == "e" or letter == "i" or letter == "u" or letter == "o":
        n += 1
    else:
        continue

print(n)

#86

pw1 = int(input("Enter a new password: "))
pw2 = int(input("Enter a new password again: "))

pw3 = pw1.lower()
pw4 = pw2.lower()

if pw1 == pw2:
    print("Thank you")
elif pw1 != pw2 and pw3 == pw4:
    print("They must be in the same case")
else:
    print("Incorrect")

#87

word = input("Enter word: ")

length = len(word)
num = 1
for i in word:
    pos = length - num
    word1 = word[pos]
    print(word1)
    num += 1
