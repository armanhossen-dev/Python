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
print(f"your lowercased name is: {name}\n") #your lowercased name is: arman hossen ripon


res = name.isdigit() # if a string contains only digits, then it will return 'True',
                     # variable.isdigit() -> this returns boolean value,
                     # if my variable contains both lettes/symbole and digits then also it will return 'False'
print(f"name.isdigit() = {res}\n") #False


res = name.isalpha() # if string only contains letters or alphabets [no white space], no digits inside it, no space
                     # variable.isalpha() also return boolean value
print(f"name.isalpha() = {res}") #name = arman  name.isalpha() = True


#lets ask for phone number
phoneNumber = input("Enter your phone number: ")

# .count("c") = this returns number of that character in a string
res = phoneNumber.count("-") #lets see how many dashs inside a number 
                             # like example: 1-234-567-8901
print(f"lets see how many '-' in your given number: r = {res}\n") # res = 3

# if phoneNumber.isdigit():
#     print("Thank you for giving your phone number!")
# else:
#     print("Your phone number should only contains digits")


# .replace() method used to replace any occurance of one char with another
# variable.replace("whatToReplace", "withWhat")
phoneNumber = phoneNumber.replace("-", "~")
print(f"Your New stylish phone number is: {phoneNumber}") # Your New stylish phone number is: 01715~649235

phoneNumber = phoneNumber.replace("~", "")
print(f"New only Digit phone number is: {phoneNumber}\n") # New only Digit phone number is: 01715649235

name = name.replace("ripon", "jibon") # name = arman hossen jibon
print(f"name = {name}")

# if i wnat to know all this methods of strings 
# print(help(str))