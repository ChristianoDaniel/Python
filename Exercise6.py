# Exercise 6 solution using lists 

# Ask the user for a string and print out whether this string is a palindrome or not. 
# A palindrome is a string that reads the same forwards and backwards.

user = str(input("String:\n"))
x = [i for i in user]
backwards = [i for i in reversed(x)]

if x == backwards:
    print("it's a palindrome")
else: 
    print("Not a palindrome")