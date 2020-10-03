# Exercise 7 solution using random library to generate test lists
import random

numlist = []
list_length = random.randint(5,15)

while len(numlist) < list_length:
    numlist.append(random.randint(1,75))

evenlist = [number for number in numlist if number % 2 == 0]

#print(list_length)
#print(numlist)
print(evenlist)