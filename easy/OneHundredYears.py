#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

age = int(input("How old are you? "))
verify = input("Have you had your birthday yet (yes/no)? ")

if verify == "yes":
	InOneHundred = 100 - age
elif verify == "no":
	InOneHundred = 99 - age
	#This will make sure that the year is right
else:
	print("you did not answer what I asked :( ")
	print("nah, I'll assume that you had your birthday")
	InOneHundred = 100 - age


Today = datetime.datetime.now()
#Gets the years on which the user will turn 100
Sum = Today.year + InOneHundred


print("You are gonna turn 100 years old in " + str(Sum))

