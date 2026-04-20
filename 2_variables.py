# variable = A container for a value ( string , integer, float, boolean )
#            A variable behaves as if it was the value it contains

# each variable should have a unique name
# to make a variable, you have to just write the variable name

# to assign a variable , you have to use = , equeal sign , 
# or assignment operator '='

# after writing the variable , you dont have to define its 
# datatype, just store the value  with proper syntax, for a string use double ""



#String -----------------------------------------------------------------------------------------
# a string is a series of text,  this can be in between double. or single qoute 

print("--------------1.String variable implementation--------------")
first_name = "Arman" 
# this can e double or single qoutes but use "" always for string!
# if i use the variable without the "" in the print funciton then that will print the variable value 
print(first_name)

#if i use the "" for the variable then it will print the variable name or not the value of the variable

# f-string:
# to use formatted string literals, begin a string with f or F before the openning quotatino mark or tripple quotatino mark,
# inside this string, you can write a Python expression between {variableName} and characters that can refer to the variables or literal vaues
# w = "World"
# print(w)
# print(f"I am inside the {w}\n")


# to format the variable in the string we use f before the "", inside the print() , here the f = means format
print(f"My First Name is {first_name}")
food = "cake"
# print(f"i like {food}")

mail = "arman@gmail.com"
print(f"My Fake mail is {mail}\n")

email = "armanhossen"
gcom = ".gmail.com"
ycom = ".yahoo.com"

name = "arman"
num = "123" #i can not use number to concat while {name+num+gcom} all 3 here have to be same datatye , here they are strings
print(f"Making a email : {name+num+gcom}\n")

print(f"My Email is {email+gcom}")
print(f"My Email is not {email+ycom}")
print(f"This is my gmail {email+gcom}")
print("\n")


#Integer -------------------------------------------------------------------------------------------------------
# integer is number without any decimal part
print("--------------2.Integer variable implementation--------------")
age = 23     # age should not be in "" then it will be string
quantity = 3 
numOfStuInCls = 50

print(f"I am now {age} years old.")
print(f"I will buy {quantity} car, Insha Allah.")
print(f"There is {numOfStuInCls} students in the class!")


#Float -----------------------------------------------------------------------------------------
# float is number with  decimal part
print("--------------3.Float variable implementation--------------")
price = 100.93
gpa = 3.50
distance = 5.5

print(f"My last semester result was {gpa}")
print(f"The price is ${price}")
print(f"I have to run {distance}km.")

laptopName = "Asus Future Model"
laptopPrice = 120500.05



#Boolean -----------------------------------------------------------------------------------------
#its binary, it can have two value only, True or False, use capital T and F starting the word True and False 
print("4.Boolean variable implementation")
Student = True
Graduate = False

# print(F"Are you a student?: {Student}")
print(F"Are you a Graduate?: {Graduate}")

haveLaptop = False
if haveLaptop:
    print("What color is your laptop?")
else:
    print("You don't have any laptop!")

forSale = True
if forSale:  #if this variable contains true then
    print("That item is for sale")
else: 
    print("That item is not available")

online = False
if online:
    print("Arman is online!")
else:
    print("Arman is offline!")

