print()
friends = 0
print(f"friends = {friends}")
friends = friends + 1   # '+' addition operator
print("friends = friends + 1")
print(f"friends = {friends}")
friends += 8            # '+=' argumented assignment operator
print("friends += 8")
print(f"friends = {friends}")
print()

friends = friends - 2
print("friends = friends - 2")
print(f"friends = {friends}")
friends -= 4            #3
print("friends -= 4")
print(f"friends = {friends}")
print()

friends = friends * 3   #9
print("friends = friends * 3")
print(f"friends = {friends}")
friends *= 2            #18  
print("friends *= 2")
print(f"friends = {friends}")
print()

friends = friends/2     #9.0
print("friends = friends/2")
print(f"friends = {friends}")
print()

# so if we devide any integer in python the next time it becomes float!!!
friends /= 3            #3.0
print("friends /= 3")
print(f"friends = {friends}")
print()
# exponens, power 
friends = friends **2   #9.0      # this is like ² of the frinds number, making square 
print("friends = friends **2 ")
print(f"friends = {friends}")
friends **= 2           #81.0     # 9² = 81.0  
print("friends **= 2")
print(f"friends = {friends}")
print()
# b = 2
# b **= 3
# print(f"b = {b}")
# print()

# modulus = give any remainder of devision
remainder = friends % 2 #1.0     # how much friend will be remain if i devide my friends number by 2  
print("remainder = friends % 2")
print(f"remainder = {remainder}")
print()

v = 9
v %= 2
print(f"v = {v}")
print()

#######################################################################
# some build in math related functions
x = 3.14
y = 4.6
z = 5.5
print("x = 3.14\ny = 4.6\nz = 5.5\n")

# --------------------------------------------------------------------
#round(variable) returns a int

#round makes the float into the  nearest int number, 
# if less than .5 then makes it to lower int number, 
# if big from .5 or same then upper int number

result  =  round(x)
print(f"result = round(x) = {result}")
# print(result) #3
result  =  round(y)
print(f"result = round(y) = {result}")
# print(result) #5 
result  =  round(z)
print(f"result = round(z) = {result}")
# print(result) #6
print()

# --------------------------------------------------------------------
#abs(variable) reutrns a possitive int 
a = -3
print("a = -3")
#absolute value of a number or variable
result = abs(a) #abs() - the absolute value is the distance between number and zero alwasy possitve
print("result = abs(a)")
print(f"result = {result}") # print(result) #3
print()

# --------------------------------------------------------------------
# pow(base, power)
print("pow(base, power)")
b = 3
print("b = 3")
result = pow(b, 4)
print(f"result = pow(b, 4) = {result}") # print(result) #81

# --------------------------------------------------------------------
# max(a, b, c, . . . ) finding max value among lots of number , it returns the max value
print("\n\nmax(a, b, c, . . . ) finding max value among lots of number , it returns the max value")
x1 = 21
y1 = 30
z1 = 23 
print("x1 = 21\ny1 = 30\nz1 = 23\n")
result = max (x1, y1, z1) 
print(f"result = max (x1, y1, z1) = {result}") #30
print()

# --------------------------------------------------------------------
# min(a,b,c, . . . ) finding min value among lots of number, it returns the min value
print("min(a,b,c, . . . ) finding min value among lots of number, it returns the min value")
x2 = 2
y2 = -1
z2 = -1.5
print("x2 = 2\ny2 = -1\nz2 = -1.5\n")
print(f"result = min(x2, y2, z2) = {result}") #-1.5
print()
# --------------------------------------------------------------------