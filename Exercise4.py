# Exercise 4

# Create a program that asks the user for a number and then prints out a list of all the divisors of...
# ...that number. A divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

user = int(input("Number: "))
x = list(range(1,user+1))

divisor = [i for i in x if user%i == 0]

print(divisor)