# using random module for health potion

import random

# choose your difficulty

print("Which difficulty would you like? [Easy, Medium, Hard]")

# first variable

difficulty1 = input('Difficulty: ').strip()

# if statement that exits if difficulty does not exist

if 'Easy' in difficulty1:
    print('Potions will heal 25-50 health')

elif 'Medium' in difficulty1:
    print('Potions will health 13-25 health')

elif 'Hard' in difficulty1:
    print('Potions will heal 8-16 health')

else:
    exit()

# assigning value to 'health' variable

health = 50

# the higher the difficulty the less health the potion will give
# assigning a list to a variable for this

difficulty2 = [1,2,3]

# another if statement referring back to the first variable to determine output
# converting all output to integers as we don't want floats in the new variable

if 'Easy' in difficulty1:
    potion_health = random.randint(25,50) / int(difficulty2[0])
    print('This time you will gain...')
    print(int(potion_health), 'health')

elif 'Medium' in difficulty1:
    potion_health = random.randint(25,50) / int(difficulty2[1])
    print('This time you will gain...')
    print(int(potion_health), 'health')

elif 'Hard' in difficulty1:
    potion_health = random.randint(25,50) / int(difficulty2[2])
    print('This time you will gain...')
    print(int(potion_health), 'health')

else:
    exit()

# assigning 'health' variable a new value by adding it to our new variable 'potion_health'

health = health + potion_health

# displays health depending on difficulty chosen

print('Your total health is now', int(health))
