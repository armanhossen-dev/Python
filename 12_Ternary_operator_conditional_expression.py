# conditional expression
#    A one-line shortcut for the if-else statement (ternary operator)
#    print or assign one of two values based on a condition
#    x if condition else y
print()
a = 5
print(f"a = {a} is positive number" if a > 0 else f"a = {a} is negative number")

res = "even" if a%2 == 1 else "odd"
print(f"a = {a} is an {res} number")
print()

num1 = -5
num2 = 55

print(f"num1 = {num1}, "+"Positive" if num1 > 0 else f"num1 = {num1}, "+ "Negative")
print(f"num2 = {num2}, "+"Positive\n" if num2 > 0 else f"num2 = {num2}, " + "Negative\n")

a1 = 8
b1 = 9
maxNum = a1 if a1>b1 else b1 
# 🫡 if i want to add this kindof condition into a big string, then i should use bracket () 
print(f"Between a1[{a1}], b1[{b1}], max number is " + ("a1" if maxNum == a1 else "b1") + f" = {maxNum}\n")

age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "a child"
print(f"You are {status}\n")

temperature = 23
weather = "hot" if temperature > 26 else "cold"
print(f"The weather is now {weather}.\n")

userRole = "admin"
access_level = "Full Access" if userRole == "admin" else "Limited Access"
print(f"You have {access_level} to the system.\n")