# types of collections in python
# collection = single "variable" used to store multiple values,
# list = [] ordered and changeable, Duplicates ok
# set = {} unordered and immutable, but Add, Remove ok, no duplicates
# Tuple = () ordered and unchangeable,  Duplicates ok,  Faster
# https://youtu.be/ix9cRaBkVe0?t=8584 

fruit = "apple"
print(fruit) # apple
print()

#list
fruits = ["apple", "banana", "coconut"]
print(fruits) # ['apple', 'banana', 'coconut']
# using index to access list items
print(f"fruits[0] = {fruits[0]}") # fruits[0] = apple
print(f"reverse print, fruits[::-1] = {fruits[::-1]}") #reverse
print()

for x in fruits:
    print(x)
    # apple
    # banana
    # coconut
print()

print("for x in fuit")
for x in fruit:
    print(x)
    # a
    # p
    # p
    # l
    # e
print()

print("for fruit in fruits:")
# here, `fruit` becomes a new loop variable
# before this loop, the fruit = "apple", but while the loop has the same variable 
# then it(fruit variable) is reused and updated repeatedly, so after the loop the last assigned value remains
for fruit in fruits:
    print(fruit)

# after the loop ends, `fruit` keeps the last value from the list
print(fruit)  # coconut

# print(dir(fruits)) # actions that fruits - list can perform
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
#  '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
#  'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# if we need description of those methods then 
# print(help(fruits))
print()
# find how many items in my list 
print(len(fruits), end="\n") # 3

# finding an element which is in the loop or not
# this returns a bool value 

print("apple" in fruits) # True
print("pinapple" in fruits) # False

# list is changeable and duplicates are ok
print(f"Before Chaneg: fruits = {fruits}")
fruits[0] = "pineapple"
fruits[1] = "mango"
print("fruits[0] = \"pineapple\"")
print("fruits[1] = \"mango\"")
print(f"After update: fruits = {fruits}\n")                   # ['pineapple', 'mango', 'coconut']

# append an item to the list, a new item will added to the end of the list
# list.append(value)
fruits.append("lychee")
print("fruits.append(\"lychee\") = ", end="")
print(fruits)                   # ['pineapple', 'mango', 'coconut', 'lychee']

# list.remove(value)
fruits.remove("coconut")
print("fruits.remove(\"coconut\") = ", end="")
print(fruits)                   # ['pineapple', 'mango', 'lychee']

# list.insert(index, value)
fruits.insert(0, "banana")
print("fruits.insert(0, \"banana\") = ", end="")
print(fruits)                   # ['banana', 'pineapple', 'mango', 'lychee']

# list.sort() # this will sort (for strings, it will make the items in alphabetic order)
fruits.sort()
print("fruits.sort() = ", end="")
print(fruits)                   # ['banana', 'lychee', 'mango', 'pineapple']

# list.revers() , this is not alphabetic reverse, its the previous orders item in reversed order
fruits.reverse()
print("fruits.reverse() = ", end="")
print(fruits)                   # ['pineapple', 'mango', 'lychee', 'banana']

# list.clear() , to clear a list all the elemnts will be gone
# fruits.clear()
# print("fruits.clear() = ", end="")
# print(f"fruits = {fruits}") # fruits = []

#find a index of a value in a list
# search index 
print(f"fruits.index(\"apple\") = {fruits.index("apple")}" if "apple" in fruits else "apple not found!") # apple not found!
print(f"fruits.index(\"banana\") = {fruits.index("banana")}" if "banana" in fruits else "banana not found!") # fruits.index("banana") = 3


# count how many same value in this list
# fruits.append("mango") 
# mc = fruits.count("mango")  # returns int
# print(mc)  # 2

print(f"fruits.count(\"banana\") = {fruits.count("banana")}") # fruits.count("banana") = 1
# https://youtu.be/ix9cRaBkVe0?t=9159