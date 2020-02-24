# basic calculator using if statements
# converts pound to kilogram and vice versa

metric = input('Are you from the us or the uk: ').strip()

if metric == 'us':
    currentWeight = input("What is your current weight in pounds?: ").strip()
    height = input('What is your height to the nearest foot?:').strip()
    lostWeight = input('How many pounds are you looking to lose?: ').strip()
    goalWeight = int(currentWeight) - int(lostWeight)
    print('Your goal weight is', goalWeight, 'pounds', 'or', (goalWeight / 2.205), 'kilograms')

elif metric == 'uk':
    currentWeight = input("What is your current weight in kilograms?: ").strip()
    height = input('What is your height to the nearest foot?:').strip()
    lostWeight = input('How many kilograms are you looking to lose?: ').strip()
    goalWeight = int(currentWeight) - int(lostWeight)
    print('Your goal weight is', goalWeight, 'kilograms', 'or', (goalWeight * 2.205), 'pounds')

else:
    print('null')
    exit()
