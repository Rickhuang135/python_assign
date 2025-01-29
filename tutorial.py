# String methods
# string = "hello world"
# type(variable) == <class 'str'>

# case operations:
# string.upper()
# string.lower()

# return number of occurences of a substring within string
# string.count('substring')

# returns the ascii (ordinal) number of a letter. Ordinal values are used when comparing strings with inequality operators
# ord('character')

# return length of string
# len(string)


# F strings (embeding variables into strings)
# x = f'hello {17%3}'
# print(x)


# ================================================================================================================


# List (Mutable Array) methods:
# array = [4, True, 'hi']
# return length of array
# len(array)

# append item to end of array
# array.append("hello")

# join one array to the end of another
# array.extend([4,5,6])

# remove and return last element in list
# last_item = array.pop()
# print(last_item)
# remove and return nth element in list
# n = 2
# nth_item = array.pop(n)
# print(nth_item)

# list copying by reference:
# array2=array
# list copying without reference:
# array3=array[:]

# array[0]="winbowoo"
# print(array)
# print(array2)
# print(array3)

# ================================================================================================================

# Tuples (Immutable Array), it is basically a read only array
# array = ("won","chew","zree")
# print(len(array))
# for item in array:
#     print(item)


# generates a type range of numbers which can be converted to type list or tuple
# set = tuple(range(0,20))
# print(set)
# print(type(set))


# list, tuple, or string slicing
# x = list(range(0,25,4))
# sliced = x[::-1]
# print(sliced)

# list, tuple, or set destructuring
# x1, x2 = (4, 5)
# print(x1, x2)

# ================================================================================================================

# sets:
# create empty set
# x=set()
# create set with items 
# y={"nmenk", "vscode", "outer"}

# add to set
# x.add("wutur")

# remove from set
# y.remove("outer")

# check for item in set
# status = "wutur" in x
# print(status)

# combine sets
# u=x.union(y)
# print(u)

# return unique elements of a set as compared to another set
# d=y.difference(x)
# print(d)

# return common elements between two sets
# i = y.intersection(x)
# print(i)

# ================================================================================================================

# dictionaries
# x = {
#     "familiar":True,
#     "satisfied": "oh man I love objects",
#     "nest":{
#         "nest":{
#             "nest":"no more"
#         }
#     }
# }
# print(x["satisfied"])

# nesting
# parent = x
# while True:
#     if "nest" in parent:
#         print("we go deeper!")
#         parent = parent["nest"]
#     else:
#         print("this is the end, where the final nested value is:")
#         print(parent)
#         break

# return values of dictionary as class "dict_values", which can be converted to list, tuple or set. Nested dictionaries are not converted, and leads to Error when converting to type set
# l=list(x.values())
# print(l)

# return keys of dictionary as class "builtin_function_or_method", which can be converted to list, tuple or set. Nested dictionaries are not converted, and leads to Error when converting to type set
# t = tuple(x.keys())
# print(t)

# delete value using key
# del x["satisfied"]
# print(x)

# returns an array of type "dict_items", in which each key and value is stored in a tuple
# li=list(x.items())
# print(type(li)

# loop through keys and items in dictionary
# for key, value in x.items():
#     print("key: ", key, "\n", "value: ", value)

# map list and tuple into dictionary
# print(dict([(1,"one"),(2,"two"),(3,"three")]))

# remove item from dictionary using key
# x.pop("satisfied")
# print(x)

# removes last item from dictionary
# x.popitem()
# print(x)

# safely retrieve item from dictionary using key without throwing error if key doesn't exist
# print(x.get("what"))

# add key with value to dictionary
# x.update({"what":"yes"})
# print(x)

# ================================================================================================================

# comprehension
# basic
# x=[x for x in range(5)]
# print(x)

# nested
# x = [[0 for x in range(5)] for x in range(20)]
# print(x)

# conditional
# x = [x for x in range(20) if x % 2]
# print(x)

# create with type tuple
# x = tuple(i for i in range(10))
# print(x)

# functions 
def func(x, y):
    return {
        "sum": x+y,
        "product": x*y,
        "exponent": x**y
    }

# storing functions in side data structures
# ar=(1,func)
# print(ar[1](1,2))

# ar = {
#     "function":func
# }
# print(ar)


# *args and **kwargs, where "kwawrgs" stands for key word arguments


# destructring lists, tuples, or sets using * prefix
# pairs = {(1,2), (3,4)}
# for pair in pairs:
#     print(func(*pair))

# destructring (unpacking string)
# x="wee"
# print(*x)

# destructring (unpacking) dictionaries with ** prefix, key names in dictionary must completely intersect with variable names inside function
# dictionary = {
#     'y': 2,
#     'x': 1,
# }
# print(func(**dictionary))

# taking in unlimited parameters using *args and **kwargs keywords
# def func(*args, **kwargs):
#     print(len(args))
#     print(type(kwargs))
#     print(*args)
# func(1,2,3,4,5,6,7,("what", "wow"),yeet=True,bleet=False)

# variables are function scoped in python
# x = "global scope"
# def func(input):
#     # print("I can print the value of x with out using global keyword: ", x)
#     global x
#     x=input
# func("function change")
# print(x)

# variables are not block scoped
# x = "global scope"
# if True:
#     x = "gl scope"
# print(x)

# ================================================================================================================

# Error handling

# raise (throw) exception
# raise Exception("I suck")
# raise FileExistsError("what")

# try except blocks
# try:
#     x=1
#     print(*x)
# except Exception as e:
#     print(e)
# finally:
#     print("put cleanup type operation here")

# ================================================================================================================

# lambda (one line anonymous function)

# map function with lambda

# l = list(range(0,20))
# mp = map(lambda x: x**2, l)
# print(list(mp))
# none anonymous alternative method
# def mapper(x):
#     return x**2
# mpalt = map(mapper,l)
# print(list(mpalt))

# filter using lambda
# fl = filter(lambda x: x % 2, l)
# print(list(fl))

# ================================================================================================================

