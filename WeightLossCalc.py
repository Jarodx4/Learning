# Don't use this I'm not a nutritionist

currentWeight = input("What is your current weight in pounds?: ")

currentHeight = input("What is your current height to the nearest foot?: ")

string = "You weigh {} and you are {} feet tall."
result = string.format(currentWeight, currentHeight)
print(result)

targetLoss = input("How much weight are you looking to lose?:" )

string = "You are looking to lose {} pounds."
loss = string.format(targetLoss)
print(loss)

lostWeight =  int(currentWeight) - int(targetLoss)

string = "Your goal weight is {}."
goalWeight = string.format(lostWeight)
print(goalWeight)

calories = 2500

string = "You would need to eat {} calories a day to achieve your goal weight of {} pounds."
diet = string.format(calories, lostWeight)
print(diet)
# To be continued
