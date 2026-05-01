# Typecasting = the processof converting a variable from one data type to another 
# using ->    str(), int(), float(), bool()
# this is especially useful while handling user input or doing any conversion


# new learnigns
nam = "Arman Hossen Ripon"
age = 23
gpa = 3.3
happy = False

print(type(age))

#type function, to get the variables type, type(variable)
print(f"\nLets See the type of the variables:\nnam = {nam} \ttype: {type(nam)}")
print(f"age = {age} \t\t\ttype: {type(age)}")
print(f"gpa = {gpa} \t\t\ttype: {type(gpa)}")
print(f"happy = {happy} \t\t\ttype: {type(happy)}")

print("\n\n")

# for changing a variables type to another type, we use typecast
# using str(), int(), float(), bool()

print(f"lets make the 'age' floating number, \nage = {float(age)}\n")
print(f"lets make the 'age' boolean, \nage = {bool(age)}\n")
print(f"lets make the 'gpa' integer number, \nage = {int(gpa)}\n")
print(f"lets make the 'happy' integer number, \nage = {int(happy)}\n")


#making a number string then adding a digit into it again make it number
target = 3504 
print("target = 3504")

target = str(target)
print("target = str(target)")

target += "1"
print(f"target += \"1\" => {target}")

target = int(target)
print("target = int(target)")
target += 1
print(f"target += 1 => {target}")
print("Sei na!...😎\n\n")


#we can use this for checking user give us his name or not! or emply input
input = ""
print("input = \"\"")
isInput = bool(input)
print(f"isInput = bool(input)\nisInput = {isInput}")

if isInput == False:
    print("You didn't Entered your input!")
else:
    print(f"Your input is : {input}")

print("\n\n\n\n")

name = "Arman Hossen"
age = 22
cgpa = 3.5
is_student = True

print(f"1.  name = {name} and type = ", type(name), "\n")
print(f"2.  age = {age} and type = "  , type(age), "\n")
print(f"3.  cgpa = {cgpa} and type = " ,  type(cgpa), "\n")
print(f"4.  is_student = {is_student} and type = " ,  type(is_student), "\n")

cgpa = int(cgpa) # now this will only store 3 not .5
print(f"5.  cgpa = {cgpa} and type = " ,  type(cgpa), "\n")


age = float(age) 
print(f"6.  age = {age} and type = ", type(age),  "\n")

age = str(age)
print(f"7.  age = {age} and type = ", type(age),  "\n")

#while name was a string variable prev, and it contains any word or letter, while converting it to boolean then it will contain True, 
# if the name variable was containing an empty string, then after converting it to boolean it will cotain false
# thats how we can check if the user entered any stirng or not!
name = bool(name)
print(f"8.  name = {name} and type = ", type(name), "\n")

emptyString = ""
emptyString = bool(emptyString)
print(f"9.  emptyString = {emptyString} and type = ", type(emptyString), "\n")