# Exercise 2

# Ask the user for a number. Depending on whether the number is even or odd.
# print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("check number: "))
check = int(input("divide number: "))

if num % 2 == 0 and num % 4 != 0:
    print("Even number")
elif num % 4 == 0:
    print("Multiple of 4")
else:
    print("Odd number")


if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num,"does not divide evenly by", check)