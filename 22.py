# types of collections in python
# collection = single "variable" used to store multiple values,
# list = [] ordered and changeable, Duplicates ok
# set = {} unordered and immutable, but Add, Remove ok, no duplicates
# Tuple = () ordered and unchangeable,  Duplicates ok,  Faster

print("\nTypes of Colllections in python:\n1. List = [value, value, value, ...]\n2. Set = {value, value, value, ...}\n3. Tuple = (value, value, value, ...)\netc.")
print("\n1. list = [], ordered as it was declared, changeable, duplicates ok ...")
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
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
 '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

# if we need description of those methods then 
# print(help(fruits))
print()
# find how many items in my list 
print(f'len(fruits) = {len(fruits)}') # 3
# finding an element which is in the loop or not
# this returns a bool value 

print(f'"apple" in fruits = {"apple" in fruits}')
# print("apple" in fruits) # True
print(f'"pinapple" in fruits = {"pinapple" in fruits}', end="\n\n") # False

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
print(f'fruits.index("apple") = {fruits.index("apple")}' if "apple" in fruits else "apple not found!") # apple not found!
print(f'fruits.index("banana") = {fruits.index("banana")}' if "banana" in fruits else "banana not found!") # fruits.index("banana") = 3

# count how many same value in this list
# fruits.append("mango") 
# mc = fruits.count("mango")  # returns int
# print(mc)  # 2

print(f'fruits.count("banana") = {fruits.count("banana")}') # fruits.count("banana") = 1
# if i want to use " inside the string then i can use the '' to f-string, like this -> print(f'string "Arman"')
print("\n----- list --- ordered and changable and duplicates are ok ------------\n")


# set
# set = {} unordered and immutable(we can alter this values), but add/remove ok, no duplicates
print("2. set = {}, unordered and immutable(we can alter theire values), but add /remove/clear same as list, no duplicates ...")
fruits2 = {"apple", "orange", "banana", "coconut"} # this is a set as {} is used and multiple values are in it
print(fruits2) # {'orange', 'apple', 'banana', 'coconut'}
                # {'orange', 'coconut', 'banana', 'apple'} // next time i run this comes 
# while we print a string it prints in an unordered way not same as the set is declared
# but if we use same set to print or use multiple time in code it will give same unordered list, but between those prints, if any 
# chaneg is made then the list will again unorder on the next print
# print(fruits2) # {'orange', 'apple', 'coconut', 'banana'}
# print(fruits2) # {'orange', 'apple', 'coconut', 'banana'}

# to display or know about all the methods of a set ,
# print(dir(fruits2))
'''
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getstate__', '__gt__','__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', 
'__isub__', '__iter__','__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
'__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
'__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint','issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
'union', 'update']
'''
# for indepth understanding of those methods we can learn thoes from 
# print(help(fruits2))

# same as list,  len(setVariable)
print(f"length = {len(fruits2)}") # length = 4
print(f'"apple" in fruits2 = {"apple" in fruits2}') # True

# in, len(setV), same as list

# but if we try to use index of set then it gives error, as its unordered so it will not work with the index
# print(fruits2[0]) # error
# we can use index with only string, list

# .add(value)
fruits2.add("pineapple")
print('fruits2.add("pineapple"): ', end="")
print(fruits2) # {'orange', 'coconut', 'banana', 'pineapple', 'apple'}

# .remove(value)
fruits2.remove("pineapple")
print('fruits2.remove("pineapple"): ', end="")
print(fruits2) # {'banana', 'orange', 'apple', 'coconut'}


# pop method is used to pop what element is on the top or last, but in set it is random
fruits2.pop()
print('fruits.pop(): ', end="")
print(fruits2) # {{'coconut', 'apple', 'banana'}

# .clear(), to clear a set
fruits2.clear()
print(fruits2) # set()

# even we add an element or value as ame before , there can be added another duplicates to the set, but when we print it it will shown one time not multiple times or in duplicatesa
alpha = {'a', 'b', 'c', 'a'}
print(alpha) # {'c', 'a', 'b'}

# those are some usefull methods, in sets
print("a set is a collection that is unordered, and unchangeable values, but add or remove can be done and no duplicates in it ------------\n\n")

# https://youtu.be/ix9cRaBkVe0?t=9360