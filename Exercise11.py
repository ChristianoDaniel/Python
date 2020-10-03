# Exericse 11

# Ask the user for a number and determine whether the number is prime or not.
# A prime number is a number that has no divisors.

number = int(input("Enter number:\n"))
check = [i for i in range(2,num) if num % i == 0]

def evaluate(n):
    if number > 1:
        if len(check) == 0:
            print("It's a prime number.")
        else:
            print("It's NOT a prime number.")
    else:
        print("It's NOT a prime number.")

evaluate(number)