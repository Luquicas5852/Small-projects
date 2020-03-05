#Create a program that gets your name and show
name = input("Tell me your full name: \n")
print("\n")

#01) The name in uppercase
print(name.upper())
print("\n")
#02) The name in lowercase
print(name.lower())
print("\n")
#03) How many letters are in the name
letters = 0
for i in range(len(name)):
    if name[i] != " ":
        letters += 1
print("Your name have {}".format(letters) + " letters")

#04) How many letter in the first name
print("Your first name is {}".format(name.split()[0]))
