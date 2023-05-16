#the % operator return the remainder of the division
# print(4%2)
# print(40%2)
# print(41%3)
#claculator
# a=int(input('enter a :'))
# b=int(input('enter b :'))
# c=input('enter operator(+,-,*,/,//) :')
# if c=='+':
#     print(a+b)
# elif c=='-':
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=='/':
#     print(a/b)
# elif c=='//':
#     print(a//b)
# else:
#     print("invalid operator")



# problems

# tax=12.5/100
# price=100.5
# tax_amount=tax*price
# total_price=price+tax_amount
# print(total_price)
# print(round(total_price,2))


#strings

#print('doesn\'t')
#Write a program that takes a list of integers as input and prints the sum, maximum, and minimum of the list.

#n=[1,2,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,18]
n=list(map(int,input('enter a list of integers seperated by space :').split(',')))
print(max(n))
print(min(n))
print(sum(n))
