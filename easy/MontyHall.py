#Create an algorithm that test the Monty Hall problem, and will show the amount of wins with and without changing.
import random

tests = int(input("Enter with the number of tests: "))
change = 0
keep = 0
for i in range(tests):
    #Generate the doors
    door = ["goat", "goat", "prize"]
    random.shuffle(door)
    any_door = random.randint(0,2)
    #don't change
    if door[any_door] == 'prize':
        keep += 1
    #Choose one
    choice = door.pop(any_door)
    door.remove('goat')
    #change
    if door[0] == 'prize':
        change += 1

how = ('changing', 'keeping')
wins = [change, keep]

print('you had {} wins by changing, and {} wins by keeping the decision'.format(change,keep))
