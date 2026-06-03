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
print(capitals.get("Bangladesh")) # Dhaka
# if key not found in the dictionary
print()
print(capitals.get("Arman")) # None


if capitals.get("japan"): # if j-> J then it would be true
    print("That capital does exists")
else:
    print("That capital dosen't exist")
    # That capital dosen't exist
    

capitals.update({"Canada":"Bogura"})
print(capitals.get("Canada")) # Bogura
print()

# print to see all the value of keys from the talbe
print(capitals) 
# {'Bangladesh': 'Dhaka', 'Ireland': 'Dublin', 'Australia': 'Canberra', 'United Kingdom': 'London', 'New Zealand':
#     'Wellington', 'China': 'Beijing', 'Korea': 'Seoul', 'Japan': 'Tokyo', 'USA': 'Washington D.C', 'India': 'New Delhi',
#     'Pakistan': 'Islamabad', 'Russia': 'Moscow', 'Peru': 'Lima', 'Canada': 'Bogura'}

print()

# remove a key and its value
capitals.pop("Canada")
print(capitals) 

# https://youtu.be/ix9cRaBkVe0?t=11256