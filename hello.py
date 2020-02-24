# This program says hello and asks for your name and age

print('Hello!')
print('What is your name?') 
myName = input().strip()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') 
myAge = input().strip()
print ('You will be ' +str(int(myAge) + 1) + ' in a year.')
