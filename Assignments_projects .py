#!/usr/bin/env python
# coding: utf-8

# In[217]:


# Assigment 1.

# Write a function solution that given a string S consisting of N letters 'a' and/or 'b' return...
# ...True when all occurrences or letter 'a' are before all occurrences of letter 'b' and returns...
# ... False otherwise.

# Examples: 
# S = "aabbb" the function should return True
# S = "ba" the function should return False. Note that 'b' does not need to occur in S
# S = "aaa" the function should return True. Note that 'a' does not need to occur in S 
# S = "b" the function should return True. 
# S = "abba" the function should return False.

# write an efficient algorithm for the following assumptions:
# N is an integer within the range [1...300,000];
# string S consist only of the characters 'a' and/or 'b'.

# create a string S 
S = str(input())

# solution function for the problem.
def solution(S):
    # checking if S contains 'a' and/or 'b' only. 
    a = [i for i in S if i != 'a']
    b = [i for i in S if i != 'b']
    a_b = len([i for i in a if i in b])
    
    # number of integer in S.
    N =len(S)
    
    # if a_b is zero, this means the string contains a and/or b, therefore 'True', otherwise 'False'.
    if a_b == 0:
        # setting the limits for N (length of string) range(1-300,000).
        while N > 0 and N <= 300000:
            # remember all 'a' must come first before 'b'. check represents the correct order for S.
            check = sorted(list(S))
            # string is 'S' as a list and the original input.
            string = list(S)
            
            # compare both string and check. if they are equal, then the string is in correct order...
            # ... it returns 'True' and breaks from the while loop. otherwise, jumps to the next...
            # ... conditon statement. Note: correct = True & incorrect = False. 
            if string == check:
                return True
                break
            # for single letters 'a' or 'b' it returns 'True', otherwise 'False'.
            elif len(string) == 1:
                return True
                break
            else: 
                return False
                break
    else: 
        return False

# call the function for final solution. 
solution(S)


# In[175]:


# Assignment 2.

# there are N coins, each showing either heads or tails. we would like all the coins...
# to form a sequence of alternating heads and tails. what is the minimum number of coins...
# that must be reversed to achhieve this? 

# write function solution(A, N)
# given that an array A consisting of N integers represeting the coins, returns the minimum...
# number of coins that must be reversed. consecutive elements of array A represent consecutive...
# coins and contain either a 0 (heads) or a 1(tails).

# Examples:
# A = [1, 0, 1, 0, 1, 1] function should return 1. after reversing the sixth coin, we achieve...
# an alternating sequence of coins [1, 0, 1, 0, 1, 0]
#
#  A = [1, 1, 0, 1, 1] function should return 2. after reversing the first and fifth coins...
# we achieve an alternating sequence [0, 1, 0, 1, 0]
#
# A = [0, 1, 0] function should return 0. the sequence of cooins is already alternating.
#
# A = [0, 1, 1, 0] function should return 2. we can reverse the first and second coins...
# to get the sequence: [1, 0, 1, 0].

# Assume that:
# N is an integer within the range [1-100]
# each element of array A is an integer that can have one of the following values: 0,1.

# create an input for list of integers. i.e. [1, 2, 3].
A = [int(i) for i in input()]

# solution function for the problem. 
def solution(A): 
    # Checking if A contains ONLY 1 and 0. If a_b = 0 therfore A contains only 1 and 0.  
    a = [i for i in A if i != 0]
    b = [i for i in A if i != 1]
    a_b = len([i for i in a if i in b])
    
    # N is the length of array A. 
    N = len(A)
    
    # count the number of changes to achieve a sequence of alternating heads and tails. 
    count = 0
    
    # for the function to work array 'A' must contain 1 and 0 only. So, a_b must be 0. 
    while a_b == 0:
        #  setting a limit for the numbers of integers in the array 'A', range (1-100). 
        while N >= 1 and N <= 100: 
            for i in range(0, N-2):
                if A[i+1] == A[i+2]:
                    if A[i+1] == A[i]:
                        if A[i+1] == 1:
                            A[i+1] = 0
                            count+=1
                        else: 
                            A[i+1] = 1
                            count+=1
                    else: 
                        if A[i+2] == 1:
                            A[i+2] = 0
                            count+=1
                        else: 
                            A[i+2] = 1
                            count+=1
              
                if A[i+1] == A[i]:
                    if A[i] == 1:
                        A[i] = 0
                        count+=1
                    else: 
                        A[i] = 1
                        count+=1
            return count       

# Calling the function for final solution. 
solution(A)  


# In[195]:


# Assignment 3.

# You are given a string S. Deetection of the K-th letter of S costs C[K]. After deleting letter...
# ... the costs of deleting other letters do not change. For exmaple, for S = "ab" and C =[1, 3]...
# ... after deleting 'a', deletion of 'b' will still cost 3. 

# You want to delete some letters from 'S' to obtain a string without atwo identical letters next...
# ... to each other. What is the minimun total cost of deletions to achieve such a string?

# write a function: solution (S, C)
# that, given string 'S' and array 'C' of integers, both of length N, returns the minimun ost of...
# ... all necessary deletions. 

# Examples:

# 1. Given S = "abccbd" and C = [0, 1, 2, 3, 4, 5], the function should return 2. you can delete...
# ... the first occurence of 'c' to acheive "abcbd".
 
# 2. Given S = " aabbcc" and C = [1, 2, 1, 2, 1, 2], the function should return 3. By deleting...
# ... all letters with a cost of 1, you can achieve string "abc".

# 3. Given S = "aaaa" and C = [3, 4, 5, 6], the function should return 12. you need to delete...
# ... all but one one letter 'a', and the lowest cost of deletions is 3+4+5 = 12. 

# 4. Given S = "ababa" and C = [10, 5, 10, 5, 10], the function should return 0. There is no...
# ... need to delete any letter. 

# Write an efficient alogorithm for the following assumptions: 

# string S and array C have length equal to N;
# N is an integer within the range [1..100,000];
# string S consists only of lowercase letters ('a' - 'Z');
# each element of array C is an integer within the range [0..1,000].


# create a input for string S and array C (*where C takes each cost followed by space).
S = input("String S: ")
C = [int(i) for i in input("array C: ").split(' ')]

def solution(S, C):
    # contains the cost of each deletion.  
    deletion_cost = []
    # N is the length of string S and array C. And 'max_cost' is the maximum cost in array C. 
    N = int(len(S))
    max_cost = max(C)
    
    # setting string S and array C length to equal N.
    while N == len(S) and len(C):
        # setting N limit range to 1-100,000.
        while N >= 1 and N <= 100000:
            # setting string S for lowercase only. 
            while S == S.lower():
                # setting a limit for each integer in array C in range 0 - 1,000. 
                while max_cost >= 0 and max_cost <= 1000:   
                    for i in range(0, N-1):
                        if list(S)[i] == list(S)[i+1]:
                            if C[i] > C[i+1]:
                                deletion_cost.append(C[i+1])
                            else: 
                                deletion_cost.append(C[i])
                    # this takes note of the cost of every deletion in string S. 
                    minimum_total_cost = sum(deletion_cost)    
                    answer = 'The minimum total cost of deletions is '
                    # returns joint string 'answer' with the minimum cost value. key: 'Concatenation'
                    return answer + str(minimum_total_cost)
# Calling function for final solution.
solution(S, C)
    


# In[191]:


d = input()
print(len(d))


# In[214]:


# Assignment 4

# you are given a table containing data. The first row contains the column headers; all the other...
#... rows contains the data. Some of the rows are defective. A row is defective if it contains at...
# ... least once cell with a 'NULL' value written in it. YOu are supposed to delete all of the...
# ... defective rows. 

# In the sample "id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11", the second row is defective...
# ... it contains a NULL in the age column. The first row (the header) is never defective. Every... 
# ... cell contains a single word. Each word may contain only digits ('0' and '9'), lowercase and ...
# ... upppercase English letters ('a' - 'z', 'A' - 'Z').

# you cannot change the order of rows. The number of rows and column may differ in different cases...
# ... the cases of the letters mattter ('a' is not equal to 'A').

# A table is given in CSV (comma-separated values) format. Every two consecutive cells in each row...
# ... are separated by a single comma ',' symbol. Every two consecutive rows are separated by a...
# ... a new-line '\n' symbol. for example, the first table from the task statement , written in ...
# ... CSV format, is the single string: "id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11". you...
# ... may assume that each row has the same number of cells. 

# Write a function: 'solution(S)'; which, given a string of S of length N, returns the table...
# ... without the defective rows in a CSV format. 

# Examples: 

# 1. Given S = "id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11", your function should return...
# ...'id,name,age,score\n17,Betty,28,11'.

# 2. Given S = "header, header\ANULL,ANNULLED\nnull,NILL\nNULL,NULL", your function should return...
# ... "header,header\nANULL,ANNULLED\nnull,NILL"

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..200,000];
# S is a string of length N in CSV format;
# There is at least one row;
# each row has the same, positive number of cells;
# each cell consist only of letters and/or digits;
# the first row does not contain a NULL cell. 


# string in CSV format.
S = "id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11"

def solution(S):
    # convert to the string to a list of all the rows. i.e. [1st row, 2nd row, 3rd row,...] 
    convert_to_list = list(S.split("\n"))
    list_of_list = [list(i.split(",")) for i in convert_to_list]
    
    # check if every cell contains single word.
    column = len(list_of_list[0])
    row = len(list_of_list)
    check = sum([len(i) for i in list_of_list])
    
    # list of lowercase alphabet.
    alpha_lw = string.ascii_lowercase
    lw = list(alpha_lw)
    #list of uppercase alphabet.
    alpha_up = string.ascii_uppercase
    upper = list(alpha_up)
    # checking for NULL in the first row.
    while 'NULL' not in list_of_list[0]:
        # checking for the same positive number of cells.
        while column*row == check:
            # checking for ONLY uppercase and lowercase included in string.
            while not S.islower() and not S.isupper():
                for item in list_of_list:
                    if "NULL" in item:
                        list_of_list.remove(item)
            
                convert_to_string = [",".join(i) for i in list_of_list]
                table = "\n".join(convert_to_string)
                return table 
# calling the fucntion for final solution.
solution(S) 


# In[100]:


b = ["John", "Charles", "Smith"]

x = ",".join(["John", "Charles", "Smith"])
x


# In[3]:


check_string = 'abccbd'

count = {}
for s in check_string:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

for key in count:
    if count[key] > 1:
        print(key, count[key])


# In[125]:


d = 'hjlslsljlPp'
z = not d.islower() and not d.isupper()
z

    


# In[4]:


import string
a_string = string.ascii_lowercase
list_a = list(a_string)

x = list(input())
j = []
for i in x: 
    if i in list_a:
        j.append('yes')
    else: 
        j.append('no')
print(j)


# In[150]:



A = [-1, -3]

def solution(A):
    #print(A)
    arrange = sorted(set(A))
    b =[i for i in range(1,max(A))]
    c = [i for i in b if i not in A]
    d = [i for i in A if i > 0] 
    
    if len(d) == 0:
        return 1
    if len(c) == 0:
        return max(A)+1
    else:
        return min(c)
solution(A)

        
    
    
    


# In[146]:


s = list(input())
s1 = [int(i) for i in s]
s1


# In[153]:


z = [True, True, True]
x = [True, False, True]
z==x


# In[169]:


a = list(input())
A =[int(i) for i in a]
b = list(input())
B = [int(i for i in b)]

def solution(A, B):
    if sum(A) > sum(B):
        
    
    


# In[ ]:




