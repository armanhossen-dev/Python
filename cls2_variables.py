# variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains
# to declare a variable just name the variable then use it or assign it with a value
from statistics import quantiles

# Strings variables and examples // string is a series of characters it can contain numbers but we treat them as strings
print("Strings Example!")
full_name = "Arman Hossen Ripon" # the statement end doesn't need any semicolon ';'
firstName = "Arman"
print(firstName)
print("firstName")
                                  #OP:
print("firstName = " + firstName) #firstName = Arman
print(f"firstName = {firstName}") #firstName = Arman , here f means format, we can use it before the "" then add variable inside "" with in {}

food = "Pizza!"
print(f"You like {food}")

email = "itis@fake.com"
print(f"Your email is {email}")
print() #this can create a newline
print()


# Integers -> An integer is an whole number, like -29394,3040,2,1,3 not fractional
print("Integers Example!")
age = 22 #don't use semicolon ';', also don't use age = "22" then technically it will be a string
quantity = 30
print(f"You are {age} years old")
print(f"You are buying {quantity} items")

numOfStudents = 40
print(f"There is {numOfStudents} students in your class")
print()
print()

# Float - contains decimal portion
print("Float Example!")
price = 10.995
gpa = 3.400
print(f"the price is ${price}")
print(f"Your GPA : {gpa}") #Your GPA : 3.4 doesn't print's the zero at the end

distance = 5.49
print(f"You ran {distance}km")

# boolean - true or false, they are binary 1,0
print("Boolean example!")
isStudent = True # the boolean value should be True or False
isRain = False
print(f"Are you a student?: {isStudent}")

if isRain:
    print("Don't go to varsity!")
else:
    print("Go to sleep")


isOnline = True
for_sale = False

if isOnline:
    print("The shop is now online")
    if for_sale:
        print("That item is for sale")
    else:
        print("That item is Not available")
else:
    print("The shop is now offline!")

