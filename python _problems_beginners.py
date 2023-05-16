# 1. Write a program that takes a list of integers as input and prints the sum, maximum, and minimum of the list.

# n=list(map(int,input('enter a list of integers seperated by space :').split(',')))
# print(max(n))
# print(min(n))
# print(sum(n))

# 2. Write a program that takes a string as input and prints its length, number of uppercase letters, number of lowercase letters, and number of digits.

b=input("enter a string :")
print(len(b))
print(sum(1 for c in b if c.isupper()))
print(sum(1 for c in b if c.islower()))
print(sum(1 for c in b if c.isdigit()))