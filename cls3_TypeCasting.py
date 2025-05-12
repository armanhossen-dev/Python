#Typecasting = the process of converting a variable from one data type to another
#function we will use : str(), int(), float(), bool() ---- alos type() to know the type of the variable

name = "Arman Hossen"
age = 22
gpa = 3.35
isStudent = True

print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(gpa)) #<class 'float'>
print(type(isStudent)) #<class 'bool'>

# lets convert type
cgpa = 3.98
cgpa = int(cgpa)
print(cgpa) # 3

price = 35
price = float(price)
print(price) # 35.0

num = 40
num = str(num)
print(f"num = {num} & num type is = {type(num)}") # num = 40 & num type is = <class 'str'>









