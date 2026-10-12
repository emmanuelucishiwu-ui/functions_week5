import random 
from functools import reduce

# A function is a self-contained, reusable block of code designed to perform a specific task.
# Think of it as a mini-program or a "machine" within a larger program: you need it information,
# it processes that information, and it gives you back a result

# def name():
#     print("Hello world")
#     print(123)
#     print(True)
  
# name()    



# amount = 10
# def name(a,b):
#     if b ==0:
#         print("Number cannot be zero")
#     print(a/b)    
  
# name(b=12, a=6)    



# def function2(a,b):
#     print(amount)
#     if a ==0:
#         print("Number cannot be zero")
#     print(b/a)    
  
# name(a=12, b=6)
# function2(b=12, a=6)    




# def function2(*args, **kwargs):
#     # print(args)
#     # print(kwargs)

#     List1 = [num for num in args if num %2 ==0]
#     dict1 = {a.upper():r for a, r in kwargs.items() if type(r) == str}
#     print(List1, dict1)

# function2(12, 6, 10, 44,  2, 5.5, False, name=12, l=6, z="Hello")   




# list1 = [12, 6, 10, 44,  2, 5.5, False]

# # list2 = ["name", "Paul", 20, True, 5+2j, 5/2, "Many", 5.5]
# list2 = ["name", "no", "Hello", True]
# def function2(*args, **kwargs):
#     list1 = list(args)
#     opp = list1.extend(list2)
#     print(opp)
#     # list1 = [num for num in list1 if num %2 ==0]

#     dict1 = {a.upper():r for a, r in kwargs.items() if type(r) == str}
#     print(list1, dict1)

# function2(12, 6, 10, 44,  2, 5.5, False, name=12, l=6, z="Hello") 





# list1 = [12, 6, 10, 44,  2, 5.5, False]

# list2 = ["name", "no", "Hello", True]
# def function2(*args, **kwargs):
#     global list1
#     list1 = list(args)
#     # list1.extend(list2)
#     # list1 = [num for num in list1 if num %2 ==0]

#     dict1 = {a.upper():r for a, r in kwargs.items() if type(r) == str}
#     print(list1, dict1)

# function2(12, 6, 10, 44,  2, 5.5, False, name=12, l=6, z="Hello") 

# print(list1)





# Lambda functions
# lambda functions are small annonymous functions that can have any number of parameter/arguments
# but only one expression, we can use for quick computation in our programs

# lambda argument : expression

# add = lambda a,b: a/b
# print(add(10, 5))

# chi = lambda a,b : random.randint(a, b)
# print(chi(0, 100))


# chi = lambda a,b,c, d: random.randint(a, b) + c -d
# print(chi(30, 100, 2, 4))



# upper_case = lambda efc: efc.upper()
# print(upper_case("hello world"))

# var = lambda a: random.randint(a, 20)

map, filter, reduce

list1 = [1,2,3,4,5]

funct = lambda a: a**a

filtered = list(map(funct,list1))
print(filtered)



list1 = [1,2,3,4,5]

funct = lambda a: a%2==0

filtered = list(filter(funct,list1))
print(filtered)



def function3(args):
    return args%3 == 0
list1 = [4,8,12,16,20,24,28,32,36,40]


filtered = list(filter(function3,list1))
print(filtered)



# reduce function applies a cumulative action to the items of an iterable from left to right.
def function4(a,b):
    return a*b

list1 = [4,8,12,16,20,24,28,32,36,40]

reduced = reduce(function4, list1)
print(reduced)
