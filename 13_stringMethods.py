name = input("Enter your full name: ")
#Arman Hossen Ripon

# len() - a funciton that will give us the length of the string.
length = len(name)
# print(type(length)) # <class 'int'>, so len() returns integer values

print(f"length of your name is {length}") 
#it counts all letters also whitespaces "Arman Hossen Ripon" = 18

# stringVariable.find("word")  to find the first occurance in that string
# what do you want to find in this name ?: 
fnd ="r"
res = name.find(fnd)
print(f"first occurance of '{fnd}' inside name is index: {res}")
# Enter your full name: Arman Hossen Ripon 
# length of your name is 18
# first occurance of 'r' inside name is index: 1

# if we need last occurance then use variable.rfind("something")
res = name.rfind("n")
print(f"last occurance of 'n' inside name is index: {res}")
# last occurance of 'n' inside name is index: 17

#if i want to capitalize the string's first letter only then use variable.capitalize()
name = name.capitalize() #this only capitalize the sentences first word's first letter only, and makes all next to lowercase
print(f"your capitalized name is: {name}") #Arman hossen ripon


name = name.upper() # this makes all the letters in that string to uppercase
print(f"your uppercased name is: {name}") #your uppercased name is: ARMAN HOSSEN RIPON


name = name.lower() # this makes all the letters into lowercase
print(f"your lowercased name is: {name}") #your lowercased name is: arman hossen ripon
# https://youtu.be/ix9cRaBkVe0?t=5489