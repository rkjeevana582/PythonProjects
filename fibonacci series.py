# fibonacci series
# a,b=10,11
# while a<50:
#     print(a)
#     a,b=b,a+b


#convert into list

# a,b=0,1
# c=()
# while a<1000:
#     c.append(a)
#     a,b=b,a+b
# print(c)

# convert into tuple

# a,b=0,1
# c=[]
# while a<10:
#     c.append(a)
#     a,b=b,a+b
# d=tuple(c)
# print(d)


#convert into set
# a,b=0,1
# c=[]
# while a<10:
#     c.append(a)
#     a,b=b,a+b
# d=set(c)
# print(d)

#convert into dictionary format
fibonacci_dict = {}  # initialize an empty dictionary

a, b = 10, 11
index = 0
while a < 1000000:
    fibonacci_dict[a] = index  # add a as a key and index as a value to the dictionary
    a, b = b, a+b
    index += 1

print(fibonacci_dict)  # print the dictionary
