# weight script
print("What is your current weight in pounds?")
currentWeight = input()
print("What is your current height to the nearest foot?")
currentHeight = input()
print(
    "So you weigh "
    + currentWeight
    + " pounds"
    + " and are "
    + currentHeight
    + " feet tall."
)
print("Are you looking to lose weight?" + " Y/N")
input()
print("If you chose Y then enter your target weight.")
print('If you chose otherwise you may exit this program.')
targetWeight = input()
print("To achieve " + targetWeight + " pounds you would need to lose... ")
print(
int(currentWeight) - int(targetWeight)
)
