# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# few example for 
#     key:value pairs
# -> id:name, item:price, 

#            country:capitals
capitals = {"Bangladesh":"Dhaka",
            "Ireland":"Dublin",
            "Australia":"Canberra",
            "United Kingdom":"London",
            "New Zealand":"Wellington",
            "China":"Beijing",
            "Korea":"Seoul",
            "Japan":"Tokyo",
            "USA":"Washington D.C",
            "India":"New Delhi",
            "Pakistan":"Islamabad",
            "Russia":"Moscow",
            "Peru":"Lima",
            "Canada":"Ottawa"}

# to see all attribute and functions for dictionary
# print(dir(capitals)) | or for description of functions -> print(help(dictionaryVariable))
'''
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault',
'update', 'values']
'''

# to get the value of key's from dictionary
print(f'1. (capitals.get(\"Bangladesh\")) = {capitals.get("Bangladesh")}') # Dhaka 
# print(variable.get(key)) = value for that key
# if key not found in the dictionary
print()

print(f'2. find "Arman" in the key: {capitals.get("Arman")}') # None

print(f'3. capitals.get(\"japan\") = {bool(capitals.get("japan"))}')

if capitals.get("japan"): # if j-> J then it would be true
    print("That capital does exists")
else:
    print("That capital dosen't exist")
    # That capital dosen't exist
print("\n")

print("Updating key Canadas value to Bogura: ")
capitals.update({"Canada":"Bogura"})
print(f"4. capitals.get('Canada') = {capitals.get('Canada')}", end="\n\n")
# print(capitals.get("Canada")) # Bogura

# print to see all the value of keys from the talbe
# print(capitals) 
# {'Bangladesh': 'Dhaka', 'Ireland': 'Dublin', 'Australia': 'Canberra', 'United Kingdom': 'London', 'New Zealand':
#     'Wellington', 'China': 'Beijing', 'Korea': 'Seoul', 'Japan': 'Tokyo', 'USA': 'Washington D.C', 'India': 'New Delhi',
#     'Pakistan': 'Islamabad', 'Russia': 'Moscow', 'Peru': 'Lima', 'Canada': 'Bogura'}
# print()

# remove a key and its value
print("remove key form the dictionary, variable.pop(value)")
print(f"capitals.pop('Canada') = {capitals.pop('Canada')}") 
# this shows the value but it also removes the key from the dictionary
print(capitals) 

# https://youtu.be/ix9cRaBkVe0?t=11268


# capitals.clear() # this will clear the dictionary


############################################# keys method ############################################

# that will return all the keys in the dictionary ! 
keys = capitals.keys()  # keys = is just a vairable

print("\n\nAll keys in this dictionary: ", end='')
print(keys)
# All keys in this dictionary: dict_keys(['Bangladesh', 'Ireland', 'Australia', 'United Kingdom', 'New Zealand', 'China', 'Korea', 'Japan', 'USA', 'India', 'Pakistan', 'Russia', 'Peru'])

# technically, key is an object, which resembles a list 
# we can use this key in for loop, they're iterable

print("\n\nUsing for loop to see the capital dictionary's keys!")
for key in capitals.keys():
    print(key)
    # Bangladesh
    # Ireland
    # Australia
    # United Kingdom
    # New Zealand
    # China
    # Korea
    # Japan
    # USA
    # India
    # Pakistan
    # Russia
    # Peru
    
############################################ values method, ############################################

# to get all the values within the dictionary! 
print()
v = capitals.values()  # v = is just a vairable, also i can use values as variable

print("Using values method to know all the values in this dictionary!")
print(v)    # dict_values(['Dhaka', 'Dublin', 'Canberra', 'London', 'Wellington', 'Beijing', 'Seoul', 'Tokyo', 'Washington D.C', 'New Delhi', 'Islamabad', 'Moscow', 'Lima'])

# using for loop to print all the values (i think they're iterable)
# yes they are!
print("\nUsing for loop to print the values!")
for val in capitals.values():
    print(val)
    # Dhaka
    # Dublin
    # Canberra
    # London
    # Wellington
    # Beijing
    # Seoul
    # Tokyo
    # Washington D.C
    # New Delhi
    # Islamabad
    # Moscow
    # Lima
print()


############################################# items method ############################################

items = capitals.items() # items = is just a vairable
# printing dictionary items 
print(items, end="\n\n") 
#  dict_items([('Bangladesh', 'Dhaka'), ('Ireland', 'Dublin'), ('Australia', 'Canberra'), ('United Kingdom', 'London'), ('New Zealand', 'Wellington'), ('China', 'Beijing'), ('Korea', 'Seoul'), ('Japan', 'Tokyo'), ('USA', 'Washington D.C'), ('India', 'New Delhi'), ('Pakistan', 'Islamabad'), ('Russia', 'Moscow'), ('Peru', 'Lima')])
# items returns a dictionary object which resembles a 2D list of tpple.
print("Dictionary list using for loop:")
num = 0
for i in capitals.items():
    num+=1
    print(f'{num:02}. {i}')
print()

print("----------------------------------------------")
print("| key                 : value                |")
print("----------------------------------------------")
for key, value in capitals.items():
    print(f'| {key: <20}: {value: <20} |')
    print("----------------------------------------------")
print()