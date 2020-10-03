# Exercise 10

# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between....
# ...the lists (without duplicates).Make sure your program works on two lists of different sizes.
# Randomly generate two lists to test this

import random

a = random.sample(range(1, 51), 30)
b = random.sample(range(5,45), 30)

num_com = [i for i in set(a) if i in b]
#result = [i for i in num_com if num_com.count(i) == 1]
print(num_com)
#print(result)
