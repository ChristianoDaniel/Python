# Exercise 1

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year they will turn 100 years old.

name = str(input("What's your name?: "))
age = int(input("What's your age?: "))
year = str(2020 + (100 - age))

print(name + "you will turn 100 years old in " + year)

num = int(input("What's the number?: "))
for i in range(0,num):
    print(name + " you will turn 100 years old in " + year)