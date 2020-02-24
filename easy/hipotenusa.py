import math

print("Enter with the sides of the right triangle: \n")
a = int(input())
b = int(input())

if (a == 0):
    print("Ops! You can't have a side with the lenght of zero! Please try again: \n")
    a = int(input())
elif (b == 0):
    print("Ops! You can't have a side with the lenght of zero! Please try again: \n")
    b = int(input())


#Find the Hypotenuse
hyp = math.sqrt(a**2 + b**2)

print("The hypotenuse is {}".format(hyp))
