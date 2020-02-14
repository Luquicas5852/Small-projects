#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num = int(input("Enter with any positive number: "))

remainder = num%2

if remainder == 0:
	print("the number " + str(num) + " is even!")
else:
	print("the number " + str(num) + " is odd!")

